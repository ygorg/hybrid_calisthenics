---
title: Library
layout: default
---

<!-- From https://github.com/midzer/urban-theme/blob/master/_includes/preview.html -->

<style>
.preview-panel {
    padding: 0.5em;
    box-sizing: border-box;
    border: 1px solid transparent;

    a{
        color: #111;
    }
    
    &:hover {
        border: 1px solid #e8e8e8;
    }
}

/* From https://vidler.app/blog/website-design/how-to-create-a-responsive-square-image-with-css/ */
.img-container {
  position: relative;
}

.img-container::after {
  content: "";
  display: block;
  padding-bottom: 100%;
}

.img-container img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 50% 50%;
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
    <div class="preview-panel">
        <a href="{{ post.url | prepend: site.baseurl }}">
                <div class="img-container">
                    <img alt="{{post.name}}" src="{{post.background}}">
                </div>
        </a>
   </div>
{% endfor %}
</div>