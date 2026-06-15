---
title: History
layout: default
sort_index: 2
---

<style>
	.hidden {
		display: none;
	}
</style>

<div id="history-container"></div>
<div id="history-editor" class="hidden">
	<textarea id="history" rows="5" cols="33"></textarea>
	<button onclick="stopEdition();">Save</button>
</div>


<button onclick="reset()">Reset</button>
<button onclick="startEdition()">Edit</button>


<script type="text/javascript" src="{{"assets/utils.js" | relative_url}}"></script>
<script type="text/javascript">
let h;

function reset() {
	h.resetHistory();
	let container = document.getElementById('history-container');
	prettyPrintHistory(container);
}

function startEdition() {
	let editor = document.getElementById('history-editor');
	let container = document.getElementById('history-container');

	document.getElementById('history').value = JSON.stringify(h.history);

	editor.classList.toggle("hidden");
	container.classList.toggle("hidden");
}

function stopEdition() {
	let editor = document.getElementById('history-editor');
	let container = document.getElementById('history-container');

	let txt = document.getElementById('history').value;
	h.history = JSON.parse(txt);
	h.saveHistory();

	prettyPrintHistory(container);

	editor.classList.toggle("hidden");
	container.classList.toggle("hidden");
}

function prettyPrintHistory(container) {
	container.innerHTML = '';
	Object.entries(h.iterPerDay()).forEach(([date, hist]) => {
		let content = hist.map((e) => `<li><a href="progression/${e['prg']}.html">${h.data[e['prg']]['name']}</a> : ${e['set']}</li>`).join('\n')

		container.innerHTML += `<h2>${date}</h2>` + "<ul>" + content + "</ul>";
	});
}

function main(hist) {
	h = hist;
	let container = document.getElementById('history-container');
	prettyPrintHistory(container);
}

function init() {
    load_movement_data(data => {
        let hist = new History();
        hist.data = data;
        main(hist);
    });
}

document.body.onload = init
</script>