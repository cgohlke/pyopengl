<!DOCTYPE html>
<html xmlns:py="http://genshi.edgewall.org/">
<head>
    <title>PyOpenGL ${version} Function Reference</title>
    <link rel="stylesheet" href="./manpage.css" type="text/css" />
    <link rel="stylesheet" href="./modern.css" type="text/css" />
    <meta charset="utf-8" /> 
</head>
<body>
<header>
<ul class="menu">
    <li><a href="/index.html">Home</a></li>
    <li><a href="/documentation/index.html">Docs</a></li>
    <li><a href="/documentation/installation.html">Install</a></li>
</ul>
<h1>PyOpenGL ${version}</h1>
</header>
<section class="jump-list">
<ul class="toc"><li py:for="package in ref.package_names()">
    <a href="#${package}">${package} Reference</a>
</li>
<li><a href="../pydoc/OpenGL.html">Overall PyDoc</a> -- includes Python-specific helper modules and the OpenGL extension modules.
	<ul class="toc">
	<li py:for="module_name,desc in implementation_module_names">
		<a href="../pydoc/OpenGL.${module_name}.html">OpenGL.${module_name} PyDoc</a> ${desc}
	</li>
	</ul>
</li>
</ul>
</section>

<section py:for="(package,sections) in ref.packages()" class="reference">
    <h2 class="package-title"><a name="${package}"/>${package} Reference</h2>
    <table><tbody><tr ><th align="right">Function</th><th>Purpose</th></tr>
    <tr py:for="name,section in sections" valign="top">
        <th align="right" class="section-name">
            <a href="${ref.url(section)}">${name}</a>
        </th>
        <td class="purpose">${section.purpose}</td>
    </tr>
    </tbody></table>
</section>

<section class="mathjax-note">
    <h2>MathML rendering</h2>
    <div><a href="http://www.mathjax.org/">
  <img title="Powered by MathJax"
       src="http://www.mathjax.org/badge.gif"
       border="0" alt="Powered by MathJax" /></a></div>
</section>
<footer>
      <ul class="menu">
        <li><a href="/index.html">Home</a></li>
        <li><a href="/documentation/index.html">Docs</a></li>
        <li><a href="/documentation/installation.html">Install</a></li>
      </ul>
<div class="metadata">This document was generated by <code>bzr branch http://bazaar.launchpad.net/%7Emcfletch/pyopengl/directdocs/</code> on ${date}</div>
</footer>
</body>
</html>

