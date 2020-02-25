{%- extends 'full.tpl' -%}

<!-- =============================================================================== -->
<!-- Rules of cell modifications                                                    -->
<!-- =============================================================================== -->

<!-- &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& --> 
<!-- Modification by tags -->
<!-- &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& -->

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
<!-- % Input -->
<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->

{%- block input_group -%}
{%- if 'hide_input' in cell['metadata'].get('tags', {}) -%}
{%- else -%}
{{ super() }}
{%- endif -%}
{%- endblock input_group -%}

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
<!-- % Any cell -->
<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->

{%- block any_cell -%}
{%- if 'hide' in cell['metadata'].get('tags', {}) or 'hide_html' in cell['metadata'].get('tags', {}) -%}

    <span if="hide"></span>

{%- elif 'solution' in cell['metadata'].get('tags', {}) -%}

    <style>
      blockquote:{background:lightgray;}
    </style>
    <div style="background:lightgray">
    	 {{ super() }}
    </div>

{%- elif 'navigation' in cell['metadata'].get('tags', {}) -%}

    <div style="background:lightgray">
    	 {{ super() }}
    </div>

{%- elif 'footnote' in cell['metadata'].get('tags', {}) -%}

    <div style="font-size:0.8em;border-top:solid black 1px">
    	 {{ super() }}
    </div>

{%- elif 'box_summary' in cell['metadata'].get('tags', {}) -%}

    <div style="background:lightgray;border:solid black 2px;pad:10px;margin-left:7em;margin-top:1em;margin-bottom:1em;">
    	 {{ super() }}
    </div>

{%- elif 'box_history' in cell['metadata'].get('tags', {}) -%}

    <div style="background:#F5CBA7;border:solid black 2px;pad:10px;margin-left:7em;margin-top:1em;margin-bottom:1em;">
    	 {{ super() }}
    </div>

{%- elif 'box_definition' in cell['metadata'].get('tags', {}) -%}

    <div style="background:lightgray;border:solid black 2px;pad:10px;margin-left:7em;margin-top:1em;margin-bottom:1em;">
    	 {{ super() }}
    </div>

{%- elif 'box_theorem' in cell['metadata'].get('tags', {}) -%}

    <div class="box_theorem">
    	 {{ super() }}
    </div>

{%- elif 'box_postulate' in cell['metadata'].get('tags', {}) -%}

    <div class="box_postulate">
    	 {{ super() }}
    </div>

{%- elif 'box_principle' in cell['metadata'].get('tags', {}) -%}

    <div class="box_principle">
    	 {{ super() }}
    </div>

{%- elif 'box_note' in cell['metadata'].get('tags', {}) -%}

    <div style="background:white;border:solid black 2px;pad:10px;margin-left:7em;margin-top:1em;margin-bottom:1em;">
    	 {{ super() }}
    </div>

{%- else -%}

    {{ super() }}

{%- endif -%}
{%- endblock any_cell -%}

<!-- =============================================================================== -->
<!-- HTML Head -->
<!-- =============================================================================== -->

{%- block html_head -%}
<meta charset="utf-8" />
<title>{{resources['metadata']['name']}}</title>

{%- if "widgets" in nb.metadata -%}
<script src="https://unpkg.com/jupyter-js-widgets@2.0.*/dist/embed.js"></script>
{%- endif-%}

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

{% for css in resources.inlining.css -%}
    <style type="text/css">
    {{ css }}
    </style>
{% endfor %}

<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}
div#notebook {
  overflow: visible;
  border-top: none;
}
{%- if resources.global_content_filter.no_prompt-%}
div#notebook-container{
  padding: 6ex 12ex 8ex 12ex;
}
{%- endif -%}
@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  }
  div.output_wrapper {
    display: block;
    page-break-inside: avoid;
  }
  div.output {
    display: block;
    page-break-inside: avoid;
  }
}
</style>

<link rel="stylesheet" href="bin/common.css">
<link rel="stylesheet" href="extras/mybook.css">

    <!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        },
      TeX: { equationNumbers: { autoNumber: "AMS" } }
    });
    </script>
    <!-- End of mathjax configuration -->
{%- endblock html_head -%}

