SCRIPT = """
const container = document.getElementById("{container_id}");
const input = document.getElementById("{widget_id}");
const fields = {fields_json};
const operators = {operators_json};
const fieldOperators = {field_operators_json};
const state = {rules_json};

function escapeHtml(value) {{
    const div = document.createElement('div');
    div.textContent = String(value);
    return div.innerHTML;
}}

function opts(list, selected) {{
    return list
        .map(([value, label]) => `<option value="${{escapeHtml(value)}}"${{value === selected ? ' selected' : ''}}>${{escapeHtml(label)}}</option>`)
        .join('');
}}

function sync() {{
    input.value = JSON.stringify(state);
}}

function isValueless(operator) {{
    return operator === 'is_null' || operator === 'is_not_null';
}}

function operatorsFor(field) {{
    return fieldOperators[field] || operators;
}}

function isGroup(node) {{
    return node !== null && typeof node === 'object' && Array.isArray(node.rules);
}}

function pathToAttr(path) {{
    return path.join('.');
}}

function attrToPath(attr) {{
    return attr === '' ? [] : attr.split('.').map(Number);
}}

function getNode(path) {{
    let node = state;
    for (const idx of path) {{
        node = node.rules[idx];
    }}
    return node;
}}

function getParentAndIndex(path) {{
    const idx = path[path.length - 1];
    const parent = getNode(path.slice(0, -1));
    return {{ parent, idx }};
}}

function defaultRule() {{
    const field = fields.length ? fields[0][0] : '';
    const fieldOps = operatorsFor(field);
    return {{ field, operator: fieldOps.length ? fieldOps[0][0] : '', value: '' }};
}}

function defaultGroup() {{
    return {{ condition: 'AND', rules: [] }};
}}

function ruleTemplate(rule, path) {{
    const pathAttr = pathToAttr(path);
    const fieldOps = operatorsFor(rule.field);
    const valueInput = isValueless(rule.operator)
        ? ''
        : `<input type="text" data-role="value" data-path="${{pathAttr}}" value="${{escapeHtml(rule.value ?? '')}}">`;

    return `
        <div class="qb-rule" data-path="${{pathAttr}}">
            <select data-role="field" data-path="${{pathAttr}}">${{opts(fields, rule.field)}}</select>
            <select data-role="operator" data-path="${{pathAttr}}">${{opts(fieldOps, rule.operator)}}</select>
            ${{valueInput}}
            <button type="button" class="qb-remove" data-role="remove-item" data-path="${{pathAttr}}">&times;</button>
        </div>
    `;
}}

function groupTemplate(group, path) {{
    const pathAttr = pathToAttr(path);
    const isRoot = path.length === 0;

    const itemsHtml = group.rules
        .map((item, idx) => {{
            const itemPath = path.concat(idx);
            return isGroup(item) ? groupTemplate(item, itemPath) : ruleTemplate(item, itemPath);
        }})
        .join('');

    const removeGroupButton = isRoot
        ? ''
        : `<button type="button" class="qb-remove qb-remove-group" data-role="remove-item" data-path="${{pathAttr}}">&times; Remove group</button>`;

    return `
        <div class="qb-group" data-path="${{pathAttr}}">
            <div class="qb-condition">
                Match
                <select data-role="condition" data-path="${{pathAttr}}">
                    <option value="AND"${{group.condition === 'AND' ? ' selected' : ''}}>ALL</option>
                    <option value="OR"${{group.condition === 'OR' ? ' selected' : ''}}>ANY</option>
                </select>
                of the following:
                ${{removeGroupButton}}
            </div>
            <div class="qb-group-items">${{itemsHtml}}</div>
            <div class="qb-group-actions">
                <button type="button" class="qb-btn" data-role="add-rule" data-path="${{pathAttr}}">+ Add rule</button>
                <button type="button" class="qb-btn qb-btn-group" data-role="add-group" data-path="${{pathAttr}}">+ Add group</button>
            </div>
        </div>
    `;
}}

function render() {{
    container.innerHTML = groupTemplate(state, []);
    attach();
    sync();
}}

function attach() {{
    container.querySelectorAll('[data-role="condition"]').forEach((sel) => {{
        sel.addEventListener('change', (e) => {{
            getNode(attrToPath(sel.dataset.path)).condition = e.target.value;
            sync();
        }});
    }});

    container.querySelectorAll('[data-role="add-rule"]').forEach((btn) => {{
        btn.addEventListener('click', () => {{
            getNode(attrToPath(btn.dataset.path)).rules.push(defaultRule());
            render();
        }});
    }});

    container.querySelectorAll('[data-role="add-group"]').forEach((btn) => {{
        btn.addEventListener('click', () => {{
            getNode(attrToPath(btn.dataset.path)).rules.push(defaultGroup());
            render();
        }});
    }});

    container.querySelectorAll('[data-role="remove-item"]').forEach((btn) => {{
        btn.addEventListener('click', () => {{
            const {{ parent, idx }} = getParentAndIndex(attrToPath(btn.dataset.path));
            parent.rules.splice(idx, 1);
            render();
        }});
    }});

    container.querySelectorAll('[data-role="field"]').forEach((sel) => {{
        sel.addEventListener('change', () => {{
            const node = getNode(attrToPath(sel.dataset.path));
            node.field = sel.value;

            const fieldOps = operatorsFor(node.field);
            const stillValid = fieldOps.some(([value]) => value === node.operator);
            if (!stillValid) {{
                node.operator = fieldOps.length ? fieldOps[0][0] : '';
            }}

            render();
        }});
    }});

    container.querySelectorAll('[data-role="operator"]').forEach((sel) => {{
        sel.addEventListener('change', () => {{
            getNode(attrToPath(sel.dataset.path)).operator = sel.value;
            render();
        }});
    }});

    container.querySelectorAll('[data-role="value"]').forEach((inp) => {{
        inp.addEventListener('input', () => {{
            getNode(attrToPath(inp.dataset.path)).value = inp.value;
            sync();
        }});
    }});
}}

render();
"""  # noqa: E501
