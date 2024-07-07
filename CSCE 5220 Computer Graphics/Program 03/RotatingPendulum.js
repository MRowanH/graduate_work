// RotatingTranslatedTriangle.js (c) 2012 matsuda, 2022 Jonathon Doran
"use strict";

const vertex_shader = `#version 300 es
    in vec4 a_Position;
	in vec4 a_Color;
	out vec4 v_Color;
    
    void main() 
    {
		v_Color = a_Color;
		gl_PointSize = 5.0;
        gl_Position = a_Position;
    }	`;


const fragment_shader = `#version 300 es
    #ifdef GL_ES
             precision mediump float;
    #endif
    in vec4 v_Color;
    out vec4 fragColor;
    
    void main() 
    {
        fragColor = v_Color;
    }	`;

// Global Variables ========================================================================

// Vertex positions
var vertices = new Float32Array([
     0.0,  0.5, 0.0, 1.0, 
	-0.5, -0.5, 0.0, 1.0, 
	 0.5, -0.5, 0.0, 0.0
    ]);

// Colors
var colors = new Float32Array([
	//1.0, 0.0, 0.0, 1.0, 
	//1.0, 0.0, 0.0, 1.0, 
	//1.0, 0.0, 0.0, 1.0
	//0.0, 1.0, 0.0, 1.0, 
	//0.0, 0.0, 1.0, 1.0
	0.0, 1.0, 0.0, 1.0
	]);
	
// Wire
const wireLen = 0.8;
const wireColor = new Float32Array([
	1.0, 0.0, 0.0, 1.0, 
	1.0, 0.0, 0.0, 1.0
	]);
	
// Anchor
const anchorPosition = new Float32Array([
	0.0, 0.0, 0.0, 1.0
	]);
const anchorColor = new Float32Array([
	0.0, 1.0, 0.0, 1.0
	]);
	
// Bob
const bobRadius = 0.1;
var bobVertices = new Float32Array([
	0.0, 0.0, 0.0, 1.0,  
	0.0, 0.0, 0.0, 1.0,  
	0.0, 0.0, 0.0, 1.0,  
	0.0, 0.0, 0.0, 1.0,  
	0.0, 0.0, 0.0, 1.0,  
	0.0, 0.0, 0.0, 1.0 
	]);
const bobColor = new Float32Array([
	0.0, 0.0, 1.0, 1.0, 
	0.0, 0.0, 1.0, 1.0, 
	0.0, 0.0, 1.0, 1.0, 
	0.0, 0.0, 1.0, 1.0, 
	0.0, 0.0, 1.0, 1.0, 
	0.0, 0.0, 1.0, 1.0 
	]);

// Rotation angle (degrees/second)
var ANGLE_STEP = 45.0;

// Main Function ===========================================================================
function main() {
	
	// Initialize WebGl and Shaders --------------------------------------------------------
	
    // Get the rendering context for WebGL
    var canvas = document.querySelector('canvas');
    const gl = canvas.getContext('webgl2');
    
    if (!gl) 
    {
        console.log('Failed to get the rendering context for WebGL');
        return;
    }

    // Initialize shaders
    if (!initShaders(gl, vertex_shader, fragment_shader))
    {
        console.log('Failed to intialize shaders.');
        return;
    }

    // Get attribute locations -------------------------------------------------------------
	
    // Get storage location of a_Color
    var a_Color = gl.getAttribLocation(gl.program, 'a_Color');
    if (!a_Color) 
    { 
        console.log('Failed to get the storage location of a_Color');
        return;
    }
	
    // Get storage location of a_Position
    var a_Position = gl.getAttribLocation(gl.program, 'a_Position');
    if (a_Position < 0) 
    { 
        console.log('Failed to get the storage location of a_Position');
        return;
    }
	
	// Set up the vertex buffer ------------------------------------------------------------
	
    // Create a buffer object
    var vertexBuffer = gl.createBuffer();
    if (!vertexBuffer) 
    {
        console.log('Failed to create the buffer object');
        return false;
    }

    // Bind the buffer object to target
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
    
    // Write date into the buffer object
    gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

    // Assign the buffer object to a_Position variable
    gl.vertexAttribPointer(a_Position, 4, gl.FLOAT, false, 0, 0);

    // Enable the assignment to a_Position variable
    gl.enableVertexAttribArray(a_Position);
	
	// Set up the color buffer -------------------------------------------------------------

    // Create a buffer object
    var colorBuffer = gl.createBuffer();
    if (!colorBuffer) 
    {
        console.log('Failed to create the buffer object');
        return false;
    }

    // Bind the buffer object to target
    gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
    
    // Write date into the buffer object
    gl.bufferData(gl.ARRAY_BUFFER, colors, gl.STATIC_DRAW);
	
    // Get storage location of a_Color
    var a_Color = gl.getAttribLocation(gl.program, 'a_Color');
    if (!a_Color) 
    { 
        console.log('Failed to get the storage location of a_Color');
        return;
    }

    // Assign the buffer object to a_Color variable
    gl.vertexAttribPointer(a_Color, 4, gl.FLOAT, false, 0, 0);

    // Enable the assignment to a_Color variable
    gl.enableVertexAttribArray(a_Color);

	// Pre-iteration setup -----------------------------------------------------------------
	
	// Get initial bob vertices
	// https://stackoverflow.com/questions/39821557/error-how-to-draw-circle-using-triangle-fan-in-webgl
	var numFans = 6;
	var anglePerFan = (2 * Math.PI) / numFans;
	var currentAngle = 0.0;
	for(var i = 0; i < numFans; i++) {
		currentAngle = anglePerFan * (i + 1);
		bobVertices[i*4] = Math.cos(currentAngle) * bobRadius + (wireLen + (bobRadius / 4)); // x
		bobVertices[i*4+1] = Math.sin(currentAngle) * bobRadius; // y
	}

    // Specify the color for clearing <canvas>
    gl.clearColor(0, 0, 0, 1);

    // Current rotation angle
    currentAngle = 0.0;
    
    // Model matrix
    var modelMatrix = new Matrix4();
	
	// Iteration ---------------------------------------------------------------------------
    var tick = function() 
    {
		// Update the rotation angle
        currentAngle = animate(currentAngle);

		// Clear <canvas>
		gl.clear(gl.COLOR_BUFFER_BIT);
		
		// Draw the triangle
        //drawTriangle(gl, 3, currentAngle, modelMatrix, vertexBuffer, colorBuffer);
		
		// Draw the wire
		drawWire(gl, currentAngle, vertexBuffer, colorBuffer);
		
		// Draw the bob
		drawBob(gl, currentAngle, modelMatrix, vertexBuffer, colorBuffer);
		
		// Draw the anchor 
		drawAnchor(gl, vertexBuffer, colorBuffer);
		
		// Request that the browser ?calls tick
        requestAnimationFrame(tick, canvas);
    };
    tick();
}

function drawBob(gl, currentAngle, modelMatrix, vertexBuffer, colorBuffer) {
	
    // Set the rotation matrix
    modelMatrix.setRotate(currentAngle, 0, 0, 1);
	
	// Get new vertices
	var newVertices = new Float32Array(bobVertices.length);
	for(var i = 0; i < 6; i++) {
		var pos = new Vector4([
			bobVertices[i*4], 
			bobVertices[i*4+1], 
			bobVertices[i*4+2], 
			bobVertices[i*4+3]
			]);
		pos = modelMatrix.multiplyVector4(pos).elements; // Dot product
		for(var j = 0; j < 4; j++) {
			newVertices[i*4+j] = pos[j];
		}
	}
	
	// 
	//console.log(modelMatrix.elements);
	//afewfa
	
	// Draw fan
	gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
	gl.bufferData(gl.ARRAY_BUFFER, newVertices, gl.STATIC_DRAW);
	
	// Color fan
	gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
	gl.bufferData(gl.ARRAY_BUFFER, bobColor, gl.STATIC_DRAW);
	
	// Draw
	gl.drawArrays(gl.TRIANGLE_FAN, 0, 7);
}

function drawWire(gl, currentAngle, vertexBuffer, colorBuffer) {
		
	// Calculate new line end point
	var line = new Float32Array([
		0.0, 0.0, 0.0, 1.0, 
		0.0, 0.0, 0.0, 1.0
		]);
	line[4] = Math.cos(currentAngle * Math.PI / 180) * wireLen;
	line[5] = Math.sin(currentAngle * Math.PI / 180) * wireLen;
	
	// Draw line
	gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
	gl.bufferData(gl.ARRAY_BUFFER, line, gl.STATIC_DRAW);
	
	// Color wire
	gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
	gl.bufferData(gl.ARRAY_BUFFER, wireColor, gl.STATIC_DRAW);
	
	// Draw
	gl.drawArrays(gl.LINES, 0, 2);
}

function drawAnchor(gl, vertexBuffer, colorBuffer) {
	
	// Draw point
	gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
	gl.bufferData(gl.ARRAY_BUFFER, anchorPosition, gl.STATIC_DRAW);
	
	// Color point
	gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
	gl.bufferData(gl.ARRAY_BUFFER, anchorColor, gl.STATIC_DRAW);
	
	// Draw
	gl.drawArrays(gl.POINTS, 0, 1);
}

function drawTriangle(gl, n, currentAngle, modelMatrix, vertexBuffer, colorBuffer) {
    // Set the rotation matrix
    modelMatrix.setRotate(currentAngle, 0, 0, 1);
	
	//var verts = new Float32Array(12);
	//for(var i = 0; i < 12; i++) {
	//	verts[i] = modelMatrix.elements[i]
	//modelMatrix.elements[0:11];
	var verts = modelMatrix.elements.slice(0, 8);
	//console.log(modelMatrix.elements);
	//lawefalewf

    // Pass the rotation matrix to the vertex shader
    //gl.uniformMatrix4fv(u_ModelMatrix, false, modelMatrix.elements);
	gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
	gl.bufferData(gl.ARRAY_BUFFER, verts, gl.STATIC_DRAW);
	
	gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
	gl.bufferData(gl.ARRAY_BUFFER, colors, gl.STATIC_DRAW);
	
    // Draw the triangle
    gl.drawArrays(gl.TRIANGLES, 0, n);
}

// Last time that this function was called
var g_last = Date.now();
function animate(angle) {
    // Calculate the elapsed time
    var now = Date.now();
    var elapsed = now - g_last;
    g_last = now;
    
    // Update the current rotation angle (adjusted by the elapsed time)
    var newAngle = angle + (ANGLE_STEP * elapsed) / 1000.0;
    return newAngle %= 360;
}

function up() {
    ANGLE_STEP += 10; 
}

function down() {
    ANGLE_STEP -= 10; 
}

/*function initVertexBuffers(gl, a_Position) {
    // Create a buffer object
    var vertexBuffer = gl.createBuffer();
    if (!vertexBuffer) 
    {
        console.log('Failed to create the buffer object');
        return false;
    }

    // Bind the buffer object to target
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
    
    // Write date into the buffer object
    gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);
	
    // Get storage location of a_Position
    var a_Position = gl.getAttribLocation(gl.program, 'a_Position');
    if (a_Position < 0) 
    { 
        console.log('Failed to get the storage location of a_Position');
        return;
    }

    // Assign the buffer object to a_Position variable
    gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, 0, 0);

    // Enable the assignment to a_Position variable
    gl.enableVertexAttribArray(a_Position);

    return true;
}

function initColorBuffer(gl, a_Color) {
    // Create a buffer object
    var colorBuffer = gl.createBuffer();
    if (!colorBuffer) 
    {
        console.log('Failed to create the buffer object');
        return false;
    }

    // Bind the buffer object to target
    gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
    
    // Write date into the buffer object
    gl.bufferData(gl.ARRAY_BUFFER, colors, gl.STATIC_DRAW);
	
    // Get storage location of a_Color
    var a_Color = gl.getAttribLocation(gl.program, 'a_Color');
    if (!a_Color) 
    { 
        console.log('Failed to get the storage location of a_Color');
        return;
    }

    // Assign the buffer object to a_Color variable
    gl.vertexAttribPointer(a_Color, 4, gl.FLOAT, false, 0, 0);

    // Enable the assignment to a_Color variable
    gl.enableVertexAttribArray(a_Color);

    return true;
}*/
