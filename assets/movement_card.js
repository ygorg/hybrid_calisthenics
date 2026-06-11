---
---

function logset(e) {
	let set = [...e.target.parentElement.getElementsByTagName('input')].map(
		e => parseInt(e.value, 10)
	).filter(e => e > 0);
	const prg_idx = e.target.parentElement.parentElement.id;
	h.logSet(prg_idx, set);
    update_level(e.target.closest('figure'))
}


function level2icon(level) {
    if (!level) {
        return '<svg width="12px" height="12px" viewBox="0 0 24 24" stroke="white" stroke-width="2" fill="none" xmlns="http://www.w3.org/2000/svg">\
                <circle cx="12" cy="12" r="9"></circle>\
                </svg>';
    }
    return '<svg width="12px" height="12px" viewBox="0 0 24 24" stroke="#90ee90" stroke-width="2" fill="none" xmlns="http://www.w3.org/2000/svg">\
            <path d="M16 9L10 15.5L7.5 13" stroke-linecap="round" stroke-linejoin="round"/>\
            <circle cx="12" cy="12" r="9"></circle>\
            </svg>';
}


function update_level(figure) {
    const prg_idx = figure.id;
    let e = figure.getElementsByClassName('prg_level')[0];
    let level = h.currentLevel(prg_idx);
    let svg = level2icon(level);
    e.innerHTML = `${svg} Level ${level || 1}`;
}

function createProgCard(prg_idx, data) {
    const prg = data[prg_idx];
    let level = h.currentLevel(prg_idx);
    let set_placeholder = prg['level'][0];
    if (h.attempted(prg_idx)) {
        set_placeholder = h.lastSet(prg_idx)['set'];
    }

    let card = "";
    card += `<figure id="${prg['prg_idx']}" class="progression-card">`;
    card += `   <img src="${prg['thumbnail']}">`;
    card += `   <figcaption>`;
    card += `       <a href="{{site.baseurl}}/progression/${prg['prg_idx']}.html">
        <span class="prg_pos">${data[prg['mvt_idx']]['name']} Progression ${prg['prg_pos']}</span>
        <span class="prg_name">${prg['name']}</span>
        <span class="prg_level">${level2icon(level)} Level ${level || 1}</span>`;
    card += `       </a>
    </figcaption>`;

    /*
    card += '<div class="logsets">';

    card += [1, 2, 3].map((i) => `<div>
    <label for="${prg['prg_idx']}-set${i}">Set ${i}</label>
    <input type="number" id="${prg['prg_idx']}-set${i}" name="${prg['prg_idx']}-set${i}" min="0" value="${set_placeholder[i-1] || 0}">
    </div>`).join('\n');

    card += '       <button>Log sets</button>\
        </div>';\*/
    card += '</figure>';
    return card;
}