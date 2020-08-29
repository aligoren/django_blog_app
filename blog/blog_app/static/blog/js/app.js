hljs.initHighlightingOnLoad();
addEventListener('DOMContentLoaded', function() {
    
    const blocks = document.querySelectorAll('pre code.hljs');

    Array.prototype.forEach.call(blocks, (block) => {
        const language = block.result.language;
        
        block.closest('pre').classList.add('formatter-code')
        
        block.insertAdjacentHTML("afterbegin",`<span class="code-language has-text-right">${language}</span>`)
    });
})