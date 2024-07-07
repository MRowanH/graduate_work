// Mica Haney
// CSCE 5220 Computer Graphics
// Final Project

"use strict";

var vertexShaderSource = `#version 300 es

// Attributes - inputs
in vec2 a_Position;
in vec2 a_TextureCoord;

// Uniforms
uniform vec2 u_Resolution;
uniform float u_FlipX;

// Outputs to fragment shader
out vec2 v_TextureCoord;

void main() {
	
	// convert from 0->2 to -1->+1 (WebGL clipspace - > HTML canvas)
	vec2 clipSpace = ((a_Position / u_Resolution) * 2.0) - 1.0;
	
	// Set pixel values and flip (if applicable)
	gl_Position = vec4(clipSpace * vec2(u_FlipX, -1), 0, 1);
	
	// Pass outputs to fragment shader
	v_TextureCoord = a_TextureCoord;
}
`;

var fragmentShaderSource = `#version 300 es

// Set precision
#ifdef GL_ES
		 precision mediump float;
#endif

// Uniforms - Texture/Image
uniform sampler2D u_Image;

// Uniforms - Convolution
uniform float u_Kernel[9];
uniform float u_KernelWeight;
uniform float u_Recolor;

// Inputs
in vec2 v_TextureCoord;

// Outputs
out vec4 outColor;

void main() {
	
	// Get size of one pixel
	vec2 onePixelSize = vec2(1) / vec2(textureSize(u_Image, 0));
	
	// Get sum of color values in convolution window
	// Get location of pixel being convolved in texture: v_TextureCoord + onePixelSize * vec2(-1, -1)
	// Access texture u_Image at location (prev comment) and get normalized RGBA: texture(u_Image, v_TextureCoord + onePixelSize * vec2(-1, -1))
	vec4 colorSum =
		texture(u_Image, v_TextureCoord + onePixelSize * vec2(-1, -1)) * u_Kernel[0] +	// Top left
		texture(u_Image, v_TextureCoord + onePixelSize * vec2( 0, -1)) * u_Kernel[1] +	// Top center
		texture(u_Image, v_TextureCoord + onePixelSize * vec2( 1, -1)) * u_Kernel[2] +	// Top right
		texture(u_Image, v_TextureCoord + onePixelSize * vec2(-1,  0)) * u_Kernel[3] +	// Center left
		texture(u_Image, v_TextureCoord + onePixelSize * vec2( 0,  0)) * u_Kernel[4] +	// Center center
		texture(u_Image, v_TextureCoord + onePixelSize * vec2( 1,  0)) * u_Kernel[5] +	// Center right
		texture(u_Image, v_TextureCoord + onePixelSize * vec2(-1,  1)) * u_Kernel[6] +	// Bottom left
		texture(u_Image, v_TextureCoord + onePixelSize * vec2( 0,  1)) * u_Kernel[7] +	// Bottom center
		texture(u_Image, v_TextureCoord + onePixelSize * vec2( 1,  1)) * u_Kernel[8];	// Bottom right
	vec3 colorFinal = (colorSum / u_KernelWeight).rgb;
	
	// Get average color value from convolution and apply recoloring (if applicable)
	if(u_Recolor == 1.0) {
		outColor = vec4(colorFinal.brg, 1);
	}
	else {
		outColor = vec4(colorFinal.rgb, 1);
	}
}
`;

// Global Variables ========================================================================

// Image url
var url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXF85Zqy4w7wDFXc11kIzUTJN87cdMz0yfEA&usqp=CAU";

// Image filters
var currentFilter = "None";
var filters = {
    None: [
      0, 0, 0,
      0, 1, 0,
      0, 0, 0,
    ],
    Blur: [
      1, 2, 1,
      2, 4, 2,
      1, 2, 1,
    ],
    Sharpen: [
       -1, -1, -1,
       -1,  9, -1,
       -1, -1, -1,
    ]
};

// Main Function ===========================================================================
function main() {
	
	// Load image from url
	var img = new Image();
	if ((new URL(url)).origin !== window.location.origin) {
		img.crossOrigin = "";
	}
	else {
		console.log("ERROR: Image does not have CORS permissions.");
	}
	img.src = url;
	img.onload = function() {
		render(img);
	};
}

function render(img) {
	
	// WebGL2 Setup ========================================================================
	
	// Initialize WebGl and Shaders --------------------------------------------------------
	
    // Get the rendering context for WebGL
    var canvas = document.querySelector("canvas");
    const gl = canvas.getContext("webgl2");
    
    if (!gl) {
        console.log("Failed to get the rendering context for WebGL");
        return;
    }
	
    // Initialize shaders
    if (!initShaders(gl, vertexShaderSource, fragmentShaderSource)) {
        console.log("Failed to intialize shaders.");
        return;
    }
	
    // Get uniform locations ---------------------------------------------------------------
	
    // Get storage location of u_Resolution
    var u_Resolution = gl.getUniformLocation(gl.program, "u_Resolution");
    if (u_Resolution < 0) { 
        console.log("Failed to get the storage location of u_Resolution");
        return;
    }
	
    // Get storage location of u_FlipX
    var u_FlipX = gl.getUniformLocation(gl.program, "u_FlipX");
    if (u_FlipX < 0) { 
        console.log("Failed to get the storage location of u_FlipX");
        return;
    }
	
    // Get storage location of u_Image
    var u_Image = gl.getUniformLocation(gl.program, "u_Image");
    if (u_Image < 0) { 
        console.log("Failed to get the storage location of u_Image");
        return;
    }
	
    // Get storage location of u_Kernel
    var u_Kernel = gl.getUniformLocation(gl.program, "u_Kernel[0]");
    if (u_Kernel < 0) { 
        console.log("Failed to get the storage location of u_Kernel");
        return;
    }
	
    // Get storage location of u_KernelWeight
    var u_KernelWeight = gl.getUniformLocation(gl.program, "u_KernelWeight");
    if (u_KernelWeight < 0) { 
        console.log("Failed to get the storage location of u_KernelWeight");
        return;
    }
	
    // Get storage location of u_Recolor
    var u_Recolor = gl.getUniformLocation(gl.program, "u_Recolor");
    if (u_Recolor < 0) { 
        console.log("Failed to get the storage location of u_Recolor");
        return;
    }
	
    // Get attribute locations -------------------------------------------------------------
	
    // Get storage location of a_Position
    var a_Position = gl.getAttribLocation(gl.program, "a_Position");
    if (a_Position < 0) { 
        console.log("Failed to get the storage location of a_Position");
        return;
    }
	
    // Get storage location of a_TextureCoord
    var a_TextureCoord = gl.getAttribLocation(gl.program, "a_TextureCoord");
    if (!a_TextureCoord) { 
        console.log("Failed to get the storage location of a_TextureCoord");
        return;
    }
	
	// Buffer variables --------------------------------------------------------------------
	var bufferSize = 2;          // 2 components from buffer per iteration
	var bufferType = gl.FLOAT;
	var bufferNormalize = false;
	var bufferStride = 0;        // Get next position
	var bufferOffset = 0;        // Start at index 0
	
	// Set up position buffer --------------------------------------------------------------
	
	// Set up vertex array
	var vertexArray = gl.createVertexArray();
	gl.bindVertexArray(vertexArray);
	gl.enableVertexAttribArray(a_Position);
	
	// Initialize the position buffer
	var positionBuffer = gl.createBuffer();
	gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
	
	// Tell a_Position how to get info out of positionBuffer
	gl.vertexAttribPointer(a_Position, bufferSize, bufferType, bufferNormalize, bufferStride, bufferOffset);
	
	// Set up texture buffer ---------------------------------------------------------------
	
	// Initialize the texture buffer
	var textureCoordBuffer = gl.createBuffer();
	gl.bindBuffer(gl.ARRAY_BUFFER, textureCoordBuffer);
	gl.enableVertexAttribArray(a_TextureCoord);
	
	// Provide coordinates of rectangle for texture
	gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([
		0,  0,	// Top left
		1,  0,	// Top right
		0,  1,	// Bottom left
		0,  1,	// Bottom left
		1,  0,	// Top right
		1,  1,	// Bottom right
		]), 
		gl.STATIC_DRAW
	);
	
	// Tell a_TextureCoord how to get elements out of textureCoordBuffer
	gl.vertexAttribPointer(a_TextureCoord, bufferSize, bufferType, bufferNormalize, bufferStride, bufferOffset);
	
	// Build Drop-Down Menu ================================================================
	
	// Create drop-down container
	var selection = document.createElement("select");
	var options = ["None", "Reflect", "Recolor", "Blur", "Sharpen"];
	for(var i = 0; i < 5; i++) {
		var opt = document.createElement("option");
		console.log(opt.value);
		if(i == 0) {
			opt.selected = true;
			}
		opt.appendChild(document.createTextNode(options[i]));
		selection.appendChild(opt);
		}
	
	// Define drop-down behaviour
	selection.onchange = function() {
		currentFilter = this.options[this.selectedIndex].value;
		handleSelection(currentFilter, img);	// Draw on change
		}
	var dropDownContainer = document.querySelector(".ddContainer");
	dropDownContainer.appendChild(selection);
	
	// Get Texture From Image ==============================================================
	
	// Set up texture 
    var tex = gl.createTexture();
	gl.activeTexture(gl.TEXTURE0 + 0);
	gl.bindTexture(gl.TEXTURE_2D, tex);
	
	// Set texture parameters 
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
	gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
	gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
	
	// Load image into the texture
	var resLevel = 0;               // Largest resolution possible
	var texColor = gl.RGBA;			// Color format of texture
	var imgColor = gl.RGBA;			// Color format of image
	var imgType = gl.UNSIGNED_BYTE;	// Data type of image
	gl.texImage2D(gl.TEXTURE_2D,
		resLevel,
		texColor,
		imgColor,
		imgType,
		img
	);
	
	// Bind the position buffer again to access the texture
	gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
	
	// Resize To Image =====================================================================
	var width = img.width;
	var height = img.height;
	
	// Resize the buffer to the image size -------------------------------------------------
	gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([
		0,		0,		// Top left
		width,	0,		// Top right
		0,		height,	// Bottom left
		0,		height,	// Bottom left
		width,	0,		// Top right
		width,	height,	// Bottom right
	]), gl.STATIC_DRAW);
	
	// Resize the canvas to the image size -------------------------------------------------
    if (canvas.width !== width ||  canvas.height !== height) {
      canvas.width  = width;
      canvas.height = height;
    } 
	else {
		console.log("ERROR: Canvas could not be resized to fit the image.");
	}
	
	// Draw Image on Canvas ================================================================
	
	// Initial draw call -------------------------------------------------------------------
	handleSelection(currentFilter, img);
	
	// Set draw variables based on selection -----------------------------------------------
	function handleSelection(name, img) {
		
		// Set variables
		var kernelName = "None";
		var flip = 1;
		var color = 0;
		switch(name) {
			case "Blur":
			case "Sharpen":
				kernelName = name;
				break;
			case "Reflect":
				flip = -1;
				break;
			case "Recolor":
				color = 1
				break;
		}
		
		// Apply variables 
		gl.uniform1f(u_FlipX, flip);
		gl.uniform1f(u_Recolor, color);
		
		// Set up to draw ------------------------------------------------------------------
		
		// Apply clipping to convert pixel coordinates to clipspace coordinates (WebGL coords -> HTML canvas coords)
		gl.viewport(0, 0, gl.canvas.width, gl.canvas.height);
		gl.uniform2f(u_Resolution, gl.canvas.width, gl.canvas.height);
		
		// Clear the canvas
		gl.clear(gl.COLOR_BUFFER_BIT);
		
		// Get program and re-bind to the vertex array
		gl.useProgram(gl.program);
		gl.bindVertexArray(vertexArray);
		
		// Get the first texture unit (original image) to modify
		gl.uniform1i(u_Image, 0);
		
		// Set up to convolve kernels across image -----------------------------------------
		
		// Set the kernel
		gl.uniform1fv(u_Kernel, filters[kernelName]);
		
		// Set kernel weight
		var weight = 0;
		for(var i = 0; i < 9; i++) {
			weight = weight + filters[kernelName][i];
		}
		gl.uniform1f(u_KernelWeight, weight);
		
		// Draw final image ----------------------------------------------------------------
		var start = 0;
		var verticies = 6;	// 6 Verticies total, 3 per triangle (2 triangles per rectangle)
		gl.drawArrays(gl.TRIANGLES, start, verticies);
	}
}