STYLE = """
.simple-qb {
    border: 1px solid var(--border-color);
    border-radius: 4px;
    background: var(--darkened-bg, var(--body-bg));
    padding: 10px;
    margin: 4px 0;
}

.simple-qb > .qb-group {
    border: none;
    padding: 0;
}

.simple-qb .qb-group-items .qb-group {
    border: 1px dashed var(--border-color);
    border-radius: 4px;
    padding: 8px;
    margin-bottom: 6px;
    background: var(--body-bg);
}

.simple-qb .qb-group-items {
    margin-left: 16px;
    padding-left: 10px;
    border-left: 2px solid var(--border-color);
}

.simple-qb .qb-condition {
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
    margin-bottom: 8px;
    font-weight: 600;
    color: var(--body-fg);
}

.simple-qb .qb-remove-group {
    margin-left: auto;
    font-weight: normal;
}

.simple-qb .qb-group-actions {
    display: flex;
    gap: 6px;
    margin-bottom: 6px;
}

.simple-qb select,
.simple-qb input[type="text"] {
    box-sizing: border-box;
    background: var(--body-bg);
    color: var(--body-fg);
    border: 1px solid var(--border-color);
    border-radius: 4px;
    padding: 4px 6px;
    font-size: 13px;
}

.simple-qb select:focus-visible,
.simple-qb input[type="text"]:focus-visible {
    outline: 2px solid var(--link-fg, #447e9b);
    outline-offset: 1px;
}

.simple-qb .qb-rule {
    display: flex;
    gap: 6px;
    align-items: center;
    margin-bottom: 6px;
}

.simple-qb .qb-rule:last-of-type {
    margin-bottom: 0;
}

.simple-qb .qb-rule input[type="text"] {
    flex: 1;
    min-width: 0;
}

.simple-qb button {
    border: none;
    border-radius: 4px;
    font-size: 12px;
    cursor: pointer;
    transition: background-color 0.15s ease;
}

.simple-qb button:focus-visible {
    outline: 2px solid var(--link-fg, #447e9b);
    outline-offset: 1px;
}

.simple-qb button.qb-btn {
    background: var(--button-bg);
    color: var(--button-fg);
    padding: 5px 10px;
    margin-top: 2px;
}

.simple-qb button.qb-btn:hover {
    background: var(--button-hover-bg);
}

.simple-qb button.qb-remove {
    background: var(--delete-button-bg, #ba2121);
    color: #fff;
    padding: 4px 8px;
}

.simple-qb button.qb-remove:hover {
    background: var(--delete-button-hover-bg, #a41515);
}
"""
