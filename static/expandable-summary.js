class ExpandableSummary extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.innerHTML = `
      <style>
        .content {
          margin-bottom: 10px;
        }

        .show-more {
          margin-top: .5em;
          text-align: center;
        }

        .show-more a {
          text-decoration: none;
          color: blue;
        }

        .show-more a:hover {
          text-decoration: underline;
          cursor: pointer;
        }
      </style>
      <div class="content-container">
        <slot name="header"></slot>
        <div class="summary">
          <slot name="summary"></slot>
        </div>
        <div class="content">
          <slot name="content"></slot>
        </div>
      </div>
      <div class="show-more">
        <a href="#" class="show-more-link">Show content...</a>
        <a href="#" class="collapse-link">Show summary...</a>
      </div>
    `;
  }

  static get observedAttributes() {
    return ['open'];
  }

  attributeChangedCallback(name, oldValue, newValue) {
    this.updateView();
  }

  get open() {
    return this.hasAttribute('open');
  }

  updateView = () => {
    const isOpen = this.open;
    this.summary.style.display = isOpen ? 'none' : 'inline';
    this.content.style.display = isOpen ? 'inline' : 'none';
    this.showMoreLink.style.display = isOpen ? 'none' : 'inline';
    this.collapseLink.style.display = isOpen ? 'inline' : 'none';
  };

  connectedCallback() {
    this.showMoreLink = this.shadowRoot.querySelector('.show-more-link');
    this.collapseLink = this.shadowRoot.querySelector('.collapse-link');
    this.summary = this.shadowRoot.querySelector('.summary');
    this.content = this.shadowRoot.querySelector('.content');

    this.updateView();

    this.showMoreLink.addEventListener('click', (event) => {
      event.preventDefault();
      this.dispatchEvent(new Event('toggle'));
    });

    this.collapseLink.addEventListener('click', (event) => {
      event.preventDefault();
      this.dispatchEvent(new Event('toggle'));
    });

    this.addEventListener('toggle', (event) => {
      this.toggleOpen();
    });
  }

  toggleOpen() {
    if (!this.open) {
      this.setAttribute('open', '');
    } else {
      this.removeAttribute('open');
    }
  }
}

customElements.define('expandable-summary', ExpandableSummary);
