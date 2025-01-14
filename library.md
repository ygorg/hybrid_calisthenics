---
title: Library
layout: default
sort_index: 1
---

<!-- From https://github.com/midzer/urban-theme/blob/master/_includes/preview.html -->

<style>
.preview-panel {
    padding: 0.5em;
    box-sizing: border-box;
    border: 1px solid #e8e8e8;
    border-radius: 10px; 

    .preview-content{
        padding-top: 70%;
    }

    .mvt_name {
        color: white;
        display: block;
    }
    .mvt_count {
        color: lightgreen;
    }

    a{
        color: #111;
    }
}

/* Grid */

.grid-wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 10px;
  margin: 0 auto;
}

@media screen and (max-width: 600px) {
    .grid-wrapper {
        grid-template-columns: 1fr 1fr;
    }
}
</style>

<div class="grid-wrapper">
{% for post in site.movement -%}
   <a href="{{ post.url | prepend: site.baseurl }}">
   <div class="preview-panel" style="background: linear-gradient(0deg, rgb(0, 0, 0, 0.6) 0%, rgb(0, 0, 0, 0.5) 30%, transparent 50%), url('{{post.background}}') center; background-size: cover;">
        <div class="preview-content">
            <span class="mvt_name">{{post.name}}</span>
            <span class="mvt_count">{{site.progression | where:"mvt_idx",post.mvt_idx | size}} Progressions</span>
        </div>
   </div>
    </a>
{% endfor %}
</div>