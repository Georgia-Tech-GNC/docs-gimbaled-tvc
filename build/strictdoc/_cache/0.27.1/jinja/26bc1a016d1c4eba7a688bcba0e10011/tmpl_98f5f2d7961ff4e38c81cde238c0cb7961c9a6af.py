from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'screens/document/document/index.jinja'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    l_0_header_items = missing
    pass
    parent_template = environment.get_template('base.jinja.html', 'screens/document/document/index.jinja')
    for name, parent_block in parent_template.blocks.items():
        context.blocks.setdefault(name, []).append(parent_block)
    l_0_header_items = ['screens/document/_shared/frame_header_document_title.jinja', 'screens/document/_shared/frame_viewtype_menu.jinja']
    context.vars['header_items'] = l_0_header_items
    context.exported_vars.add('header_items')
    yield from parent_template.root_render_func(context)

def block_head_css(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_super = context.super('head_css', block_head_css)
    _block_vars = {}
    pass
    yield '\n  '
    yield escape(context.call(l_0_super, _block_vars=_block_vars))
    yield '\n'

def block_head_scripts(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_super = context.super('head_scripts', block_head_scripts)
    _block_vars = {}
    l_0_view_object = resolve('view_object')
    pass
    yield '\n  \n  <script src="'
    yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'app_core.js', _block_vars=_block_vars))
    yield '"></script>\n\n  <script src="'
    yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'dropdown_menu.js', _block_vars=_block_vars))
    yield '"></script>\n\n  <script src="'
    yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'resizable_bar.js', _block_vars=_block_vars))
    yield '"></script>\n  <script src="'
    yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'collapsible_toc.js', _block_vars=_block_vars))
    yield '"></script>\n  <script src="'
    yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'project_tree_preserve_scroll.js', _block_vars=_block_vars))
    yield '"></script>\n  <script src="'
    yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'toc_highlighting.js', _block_vars=_block_vars))
    yield '"></script>\n\n  <script src="'
    yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'copy_to_clipboard.js', _block_vars=_block_vars))
    yield '"></script>\n\n  '
    template = environment.get_template('_shared/static_search_head.jinja', 'screens/document/document/index.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'super': l_0_super}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    if environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'is_running_on_server'):
        pass
        yield '<script type="module">\n    import hotwiredTurbo from "'
        yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'turbo.min.js', _block_vars=_block_vars))
        yield '";\n  </script>\n\n  <script src="'
        yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'autocompletable_field.js', _block_vars=_block_vars))
        yield '"></script>\n\n  '
        if (not context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'has_included_document'), _block_vars=_block_vars)):
            pass
            yield '\n  <script src="'
            yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'draggable_list.js', _block_vars=_block_vars))
            yield '"></script>\n  '
        yield '\n  <script src="'
        yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'editable_field.js', _block_vars=_block_vars))
        yield '"></script>\n  <script src="'
        yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'deletable_field.js', _block_vars=_block_vars))
        yield '"></script>\n  <script src="'
        yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'movable_field.js', _block_vars=_block_vars))
        yield '"></script>\n  <script src="'
        yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'modal.js', _block_vars=_block_vars))
        yield '"></script>\n  <script src="'
        yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'scroll_into_view.js', _block_vars=_block_vars))
        yield '"></script>\n  <script src="'
        yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'tabs.js', _block_vars=_block_vars))
        yield '"></script>\n  <script src="'
        yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'action_button_guard.js', _block_vars=_block_vars))
        yield '"></script>'
    if context.call(environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'project_config'), 'is_activated_mathjax'), _block_vars=_block_vars):
        pass
        yield '<script>\n  // configure mathjax to show equation numbers\n  window.MathJax = {\n    tex: {\n      tags: \'ams\',\n    },\n    startup: {\n      // Defer the initial typeset off the critical render path:\n      // it is kicked at browser idle time below.\n      typeset: false,\n    },\n  };\n  // Typeset when the browser is idle instead of blocking first paint.\n  // Race handling: the MathJax script is loaded async, so when the idle\n  // callback fires it can be in one of three states:\n  // 1. fully started:    typesetPromise exists -> typeset directly;\n  // 2. loaded, starting: startup.promise exists -> typeset once startup\n  //                      is complete;\n  // 3. not executed yet: window.MathJax is still the plain config object\n  //                      above (no startup.promise) -> re-check shortly.\n  window.addEventListener(\'load\', () => {\n    const kickMathJax = () => {\n      if (window.MathJax?.typesetPromise) {\n        MathJax.typesetPromise().catch(console.error);\n      } else if (window.MathJax?.startup?.promise) {\n        MathJax.startup.promise\n          .then(() => MathJax.typesetPromise())\n          .catch(console.error);\n      } else {\n        setTimeout(kickMathJax, 100);\n      }\n    };\n    (\'requestIdleCallback\' in window)\n      ? requestIdleCallback(kickMathJax, { timeout: 2000 })\n      : setTimeout(kickMathJax, 0);\n  });\n  </script>\n  <script id="MathJax-script" async src="'
        yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'mathjax/tex-mml-chtml.js', _block_vars=_block_vars))
        yield '"></script>'
        if environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'is_running_on_server'):
            pass
            yield '<script>\n    // edits can break equation numbering, requiring a full MathJax re-typeset().\n    // To allow MathJax to reparse, the server stores the original math in an extra\n    // \'original-math\' attribute on each affected div/span. This function then restores\n    // the original DOM state, for reprocessing.\n    function restoreOriginalMathElements(root = document)\n    {\n      // Select all div or span elements with class \'math\' and an \'original-math\' attribute\n      const mathElements = root.querySelectorAll(\'div.math[original-math], span.math[original-math]\');\n\n      mathElements.forEach(el => {\n        const original = el.getAttribute(\'original-math\');\n        if (original !== null) {\n            // Restore the original content\n            el.innerHTML = original;\n        }\n      });\n    }\n\n    // This EventListener will hook to node updates and re-typeset the MathJax expressions (i.e. after saving)...\n    document.addEventListener("turbo:before-stream-render", (event) => {\n      if (window.MathJax?.typesetPromise) {\n        requestAnimationFrame(() => {\n          restoreOriginalMathElements();                 // restore all math divs and spans in the DOM\n          MathJax.texReset();                            // reset all previous tex input state (eq numbering...) \n          MathJax.typesetClear();                        // remove all previous output state (typesetting, elements...)\n          MathJax.typesetPromise().catch(console.error); // typeset again, this re-creates the equation numbers\n        });\n      }\n    });  \n  </script>'
    if context.call(environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'project_config'), 'is_activated_mermaid'), _block_vars=_block_vars):
        pass
        yield '<script src="'
        yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'render_static_url'), 'mermaid/mermaid.min.js', _block_vars=_block_vars))
        yield '"></script>\n    <script type="module">\n      // Defer the initial diagram rendering off the critical render path.\n      // mermaid.min.js is a classic script loaded before this module, so\n      // the mermaid global is guaranteed to exist here (no load race,\n      // unlike the async MathJax script above).\n      mermaid.initialize({ startOnLoad: false });\n      window.addEventListener(\'load\', () => {\n        const kickMermaid = () => mermaid.run().catch(console.error);\n        (\'requestIdleCallback\' in window)\n          ? requestIdleCallback(kickMermaid, { timeout: 2000 })\n          : setTimeout(kickMermaid, 0);\n      });\n    </script>'
        if environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'is_running_on_server'):
            pass
            yield '<script>\n      // Re-run mermaid after node updates (i.e. after saving)...\n      document.addEventListener("turbo:before-stream-render", () => {\n        requestAnimationFrame(() => mermaid.run());\n      });\n    </script>'
    yield escape(context.call(l_0_super, _block_vars=_block_vars))
    yield '\n'

def block_title(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    l_0_view_object = resolve('view_object')
    pass
    yield escape(environment.getattr(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'document'), 'title'))
    yield ' - '
    yield escape(context.call(environment.getattr((undefined(name='view_object') if l_0_view_object is missing else l_0_view_object), 'get_page_title'), _block_vars=_block_vars))

def block_viewtype(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    pass
    yield 'document'

def block_layout_nav(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    pass
    yield '\n  '
    template = environment.get_template('_shared/nav.jinja.html', 'screens/document/document/index.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'

def block_tree_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    pass
    yield '\n  '
    template = environment.get_template('screens/document/_shared/resizable_bar_with_project_tree.jinja', 'screens/document/document/index.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'

def block_toc_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    pass
    yield '\n  '
    template = environment.get_template('screens/document/_shared/resizable_bar_with_toc.jinja', 'screens/document/document/index.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'

def block_header_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    l_0_header_items = resolve('header_items')
    pass
    l_1_header__items = (undefined(name='header_items') if l_0_header_items is missing else l_0_header_items)
    l_1_header__last = 'screens/document/document/actions.jinja'
    pass
    template = environment.get_template('components/header/index.jinja', 'screens/document/document/index.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {'header__items': l_1_header__items, 'header__last': l_1_header__last}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    l_1_header__items = l_1_header__last = missing

def block_main_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    pass
    yield '\n  '
    template = environment.get_template('screens/document/document/main.jinja', 'screens/document/document/index.jinja')
    gen = template.root_render_func(template.new_context(context.get_all(), True, {}))
    try:
        for event in gen:
            yield event
    finally: gen.close()
    yield '\n'

blocks = {'head_css': block_head_css, 'head_scripts': block_head_scripts, 'title': block_title, 'viewtype': block_viewtype, 'layout_nav': block_layout_nav, 'tree_content': block_tree_content, 'toc_content': block_toc_content, 'header_content': block_header_content, 'main_content': block_main_content}
debug_info = '1=13&155=16&3=21&4=31&7=34&9=45&11=47&13=49&14=51&15=53&16=55&18=57&20=59&22=65&24=68&27=70&29=72&30=75&32=78&33=80&34=82&35=84&36=86&37=88&38=90&41=92&79=95&80=97&114=100&115=103&129=105&138=108&140=111&141=124&143=134&144=143&147=151&148=160&151=168&152=177&161=185&166=197&170=205&171=214'