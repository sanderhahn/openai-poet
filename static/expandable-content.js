class ExpandableContent extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.innerHTML = `
      <style>
        .content-container {
          max-height: 200px;
          overflow: hidden;
          transition: max-height 0.3s ease;
        }

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
        <div class="content">
          <slot name="content"></slot>
        </div>
      </div>
      <div class="show-more">
        <a href="#" class="show-more-link">Show more...</a>
        <a href="#" class="collapse-link">Collapse...</a>
      </div>
    `;
  }

  connectedCallback() {
    const showMoreLink = this.shadowRoot.querySelector('.show-more-link');
    const collapseLink = this.shadowRoot.querySelector('.collapse-link');
    const contentContainer = this.shadowRoot.querySelector('.content-container');

    const isOpen = this.hasAttribute('open'); // Check if "open" attribute is present
    contentContainer.style.maxHeight = isOpen ? 'none' : '200px';
    showMoreLink.style.display = isOpen ? 'none' : 'inline';
    collapseLink.style.display = isOpen ? 'inline' : 'none';

    showMoreLink.addEventListener('click', (event) => {
      event.preventDefault();
      contentContainer.style.maxHeight = 'none';
      showMoreLink.style.display = 'none';
      collapseLink.style.display = 'inline';
      this.setAttribute('open', ''); // Add the "open" attribute
      this.dispatchEvent(new Event('toggle')); // Dispatch the "toggle" event
    });

    collapseLink.addEventListener('click', (event) => {
      event.preventDefault();
      contentContainer.style.maxHeight = '200px';
      showMoreLink.style.display = 'inline';
      collapseLink.style.display = 'none';
      this.removeAttribute('open'); // Remove the "open" attribute
      this.dispatchEvent(new Event('toggle')); // Dispatch the "toggle" event
    });
  }
}

customElements.define('expandable-content', ExpandableContent);
