function renderBubbleChart(){

    var diameter = 960,
    	format = d3.format(",d"),
    	color = d3.scale.category20c();

    var bubble = d3.layout.pack()
    	.sort(null)
    	.size([diameter, diameter])
    	.padding(1.5);

    var svg = d3.select("body").append("svg")
    	.attr("id", "svg-main")
    	.attr("width", diameter)
    	.attr("height", diameter)
    	.attr("class", "bubble");

    d3.json("../static/bubble.json", function(error, root) {
    		var node = svg.selectAll(".node")
    			.data(bubble.nodes({children: root}))
    		.enter().append("g")
    	    .attr("class", "node")
    	    .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

    node.append("title")
        .text(function(d) { return d.className + ": " + format(d.value); });

    node.append("circle")
    	.attr("class", "citybubble")
        .attr("r", function(d) { return d.r; })
        .style("fill", function(d) { return color(d.packageName); })
        .on("mouseover", function(d) {
        	console.log(d);
        	d3.select(this.parentNode)
        		.append("text")
    		    .attr("dy", "1.5em")
    		    .style("text-anchor", "middle")
        		.attr("id", "tooltip")
        		.text(d.value);
        })
        .on("mouseout", function(d) {
        	svg.select("#tooltip").remove();
        });
        // .call(d3.helper.tooltip()
        // 	.attr({class: function(d){return value}})
        // 	.style({color: 'blue'})
        // 	.text(function(d){ return 'pop: ', value
        // })
        // )	

    node.append("text")
    	.attr("class", "bubbletext")
        .attr("dy", ".3em")
        .style("text-anchor", "middle")
        .text(function(d) { return d.className; })
    });

    d3.select(self.frameElement).style("height", diameter + "px");

};