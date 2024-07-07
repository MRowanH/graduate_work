// Vertex shader program
  const vertexShader = `#version 300 es
   uniform float u_PointSize;
  in vec3 a_Position;
  in vec3 a_Color;
  out vec4 v_Color;
  void main() {
    v_Color = vec4(a_Color, 1);
    gl_Position = vec4(a_Position, 1);
    gl_PointSize = u_PointSize;
  }`

// Fragment shader program
  const fragmentShader = `#version 300 es
  precision mediump float;
  in vec4 v_Color;
  out vec4 color;
  void main() {
    color = v_Color;
  }`

function main() {
	// Get the rendering context for WebGL
	const gl = document.querySelector('canvas').getContext('webgl2');
	if (!gl) {
		console.log('Failed to get the rendering context for WebGL');
		return;
	}
	
	// Compile the vertex shader
	const vs = gl.createShader(gl.VERTEX_SHADER);
	gl.shaderSource(vs, vertexShader);
	gl.compileShader(vs);

	// Compile the fragment shader
	const fs = gl.createShader(gl.FRAGMENT_SHADER);
	gl.shaderSource(fs, fragmentShader);
	gl.compileShader(fs);
  
	// Link the program
	const pro = gl.createProgram();
	gl.attachShader(pro, vs);
	gl.attachShader(pro, fs);
	gl.linkProgram(pro);
	if (!gl.getProgramParameter(pro, gl.LINK_STATUS)) {
		console.error('prog info-log:', gl.getProgramInfoLog(prog));
		console.error('vert info-log: ', gl.getShaderInfoLog(vs));
		console.error('frag info-log: ', gl.getShaderInfoLog(fs));
	}
  
	// Use the program
	gl.useProgram(pro);
  
	// Get attributes
	const pSize = gl.getUniformLocation(pro, 'u_PointSize');
	const pos = gl.getAttribLocation(pro, 'a_Position');
	const col = gl.getAttribLocation(pro, 'a_Color');
  
	// Set up attribute buffers
	const pBuffer = gl.createBuffer();
	const cBuffer = gl.createBuffer();
  
	// Set up a vertex array object
	const vao = gl.createVertexArray();
	gl.bindVertexArray(vao);
  
	// Pull 3 floats at a time out of the position buffer
	gl.bindBuffer(gl.ARRAY_BUFFER, pBuffer);
	gl.enableVertexAttribArray(pos);
	gl.vertexAttribPointer(pos, 3, gl.FLOAT, false, 0, 0);
  
	// Pull 3 floats at a time out of the color buffer
	gl.bindBuffer(gl.ARRAY_BUFFER, cBuffer);
	gl.enableVertexAttribArray(col);
	gl.vertexAttribPointer(col, 3, gl.FLOAT, false, 0, 0);
  
	// Set uniform value
	gl.uniform1f(pSize, 1);
  
	// Set up the initial 4 points
	var startPositions = new Float32Array([
		-0.9, -0.9, 0.0, 
		0.0, 0.9, 0.0, 
		0.9, -0.9, 0.0,
		0.1, 0.1, 0.0		// Seed
	]);
	var startColors = new Float32Array([
		1.0, 0.0, 0.0, 
		0.0, 1.0, 0.0, 
		0.0, 0.0, 1.0, 
		0.0, 0.0, 0.0	// Seed, invisible
	]);
	
	
	// Set up tracking arrays
	const n = 50000.0;
	var positions = new Float32Array(n * 3 + 12);
	var colors = new Float32Array(n * 3 + 12);
	
	// Set up iteration
	var idx;
	var v = new Float32Array(3);
	var d;
	var min_d;
	for(var i = 0; i < n + 4; i++) {
		
		// Add initial points
		if(i < 4) {
			for(var j = 0; j < 3; j++) {
				positions[i*3+j] = startPositions[i*3+j];
				colors[i*3+j] = startColors[i*3+j];
			}
		}
			
		// Add calculated points
		else {
			min_d = 10.0;
				
			// Select traiangle vertex
			idx = Math.floor(Math.random()*3.0);
			for(var j = 0; j < 3; j++) {
				v[j] = positions[idx*3+j];
				
				// Calculate new positions
				if(v[j] < positions[(i-1)*3+j]) {
					positions[i*3+j] = (positions[(i-1)*3+j] - v[j]) / 2.0 + v[j];
				}
				else {
					positions[i*3+j] = (v[j] - positions[(i-1)*3+j]) / 2.0 + positions[(i-1)*3+j];
				}
			}
			
			// Calculate new colors
			for(var j = 0; j < 3; j++) {
				d = calcDistance(positions[i*3], positions[i*3+1], positions[j*3], positions[j*3+1]);
				if(d < min_d) {
					min_d = d;
					idx = j
				}
			}
			for(var j = 0; j < 3; j++) {
				colors[i*3+j] = colors[idx*3+j];
			}
		}
	}
	
	// Bind the buffers
	gl.bindBuffer(gl.ARRAY_BUFFER, pBuffer);
	gl.bufferData(gl.ARRAY_BUFFER, positions, gl.STATIC_DRAW);
	gl.bindBuffer(gl.ARRAY_BUFFER, cBuffer);
	gl.bufferData(gl.ARRAY_BUFFER, colors, gl.STATIC_DRAW);
  
	// Draw the points
	gl.clearColor(0, 0, 0, 1);
	gl.clear(gl.COLOR_BUFFER_BIT);
	gl.drawArrays(gl.POINTS, 0, positions.length / 3);
}

function calcDistance(v1_x, v1_y, v2_x, v2_y) {
	return (v2_x - v1_x) ** 2 + (v2_y - v1_y) ** 2;
}