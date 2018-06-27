# HEXO BLOG
---

## Install

- Install `Yarn`/`npm` & `Hexo`

    ```bash
    # Yarn
    brew install yarn
    yarn global add hexo-cli
    # npm 
    npm install hexo-cli -g
    ```

- Init Hexo & Run

    ```bash
    hexo init blog
    cd blog
    # npm install
    hexo generate
    hexo server
    ```

- Writing

  ```bash
  hexo new draft <title>
  hexo new <post-title>
  ```

## Hexo

> [Hexo Docs](https://hexo.io/docs/)

- Quick Start

    ```bash
    hexo new "New Post"     # Create a new post
    hexo server             # Run Server (localhost:4000)
    hexo -p 8000 --debug
    
    hexo generate           # Generate static files
    hexo deploy             # Deploy to remote sites
    hexo clean              # Clean cache files

    hexo new post <title> 
    hexo new page tags
    ```

- Plugin
    - [Hexo Plugin](https://hexo.io/plugins/)

    ```bash
    yarn add <plugin>
    ```

    ```json
    "dependencies": {
      "gulp": "^3.9.1",
      "gulp-clean-css": "^3.9.4",
      "gulp-htmlclean": "^2.7.22",
      "gulp-htmlmin": "^4.0.0",
      "gulp-imagemin": "^4.1.0",
      "gulp-minify-css": "^1.2.4",
      "gulp-uglify": "^3.0.0",
      "hexo": "^3.2.0",
      "hexo-abbrlink": "^2.0.5",
      "hexo-addlink": "^1.0.4",
      "hexo-autonofollow": "^1.0.1",
      "hexo-deployer-git": "^0.3.1",
      "hexo-filter-auto-spacing": "^0.2.1",
      "hexo-generator-archive": "^0.1.5",
      "hexo-generator-category": "^0.1.3",
      "hexo-generator-feed": "^1.2.2",
      "hexo-generator-index": "^0.2.1",
      "hexo-generator-searchdb": "^1.0.8",
      "hexo-generator-tag": "^0.2.0",
      "hexo-pdf": "^1.1.1",
      "hexo-renderer-marked": "^0.3.2",
      "hexo-renderer-stylus": "^0.3.3",
      "hexo-server": "^0.2.0"
    }
    ```

    - Details
        - `hexo-filter-auto-spacing`: Add spaces between CJK characters and western characters.
        - `hexo-pdf`: Hexo tag for embeded pdf

- Configs
    - When we say **`hexo config`** means the hexo project config
        - PATH: `/hexo/_config.yml`
    - When we say **`themes config`** means the config of theme **`NexT`**. But we want to separate the config from the theme source files, we will fully override default configuration.
        - Original PATH: `/hexo/themes/next/_config.yml`
        - Real PATH: `/hexo/source/_data/next.yml`

## Hexo config

- Default: `_config.yml`
    - `hexo --config custom.yml`

    ```yaml
    # 文章链接唯一化: hexo-abbrlink
    permalink: posts/:abbrlink/
    abbrlink:
      alg: crc32
      rep: hex

    # Markdown 渲染引擎: hexo-renderer-marked
    marked:
      gfm: true
      pedantic: false
      sanitize: false
      tables: true
      breaks: true
      smartLists: true
      smartypants: true

    # Git 自动部署: hexo-deployer-git
    deploy:
      type: git
      repo: https://github.com/lzsdodo/blog
      branch: hexo-dev
      message: "Site updated: {{now('YYYY-MM-DD HH:mm:ss')}})"
    ```

- 页面文章篇数: `hexo-generator-index/archive/category/tag`

    ```
    index_generator:
      path: ''
      per_page: 10
      order_by: -date
      
    archive_generator:
      per_page: 20
      yearly: true
      monthly: true

    category_generator:
      per_page: 10

    tag_generator:
      per_page: 10
    ```

- Search: `hexo-generator-searchdb`

    ```
    search:
      path: search.xml
      field: post
      format: html
      limit: 10000
    ```

- RSS: `hexo-generator-feed`

    ```
    feed:
      type: atom
      path: atom.xml
      limit: 20
    ```

- Adding current post link in hexo post page: `hexo-addlink`

  ```
  addlink:
    before_text: hello  # text before the post link
    after_text: bye     # text after the post link
  ```

- Sitemap: `hexo-generator-seo-friendly-sitemap`

    ```
    sitemap:
      path: sitemap.xml
    ```

## Theme Config

- Theme: NexT

    ```bash
    git clone https://github.com/theme-next/hexo-theme-next themes/next
    ```

    ```
    # Hexo config
    theme: next
    ```


- Configs
  - Original config: `vi /hexo/themes/next/_config.yml`
  - Real config: `vi /hexo/source/_data/next.yml`

    ```
    override: true
    ```

- `theme-next-fancybox3`
  
    ```bash
    cd themes/next/
    git clone https://github.com/theme-next/theme-next-fancybox3 source/lib/fancybox
    ```

    ```yaml
    # Real theme config
    fancybox: true
    ```

- `hexo-pdf`: 

    ```html
    {% pdf ./bash_freshman.pdf %}
    {% pdf https://drive.google.com/file/d/xxx/preview %}
    {% pdf http://domain.com/example.pdf %}
    ```

## Optim

> Compress resources with `gulp`

- Install 

    ```bash
    yarn global add gulp-cli
    yarn add gulp-clean-css gulp-uglify gulp-htmlmin gulp-htmlclean gulp-imagemin gulp
    ```

- Config: `gulpfile.js`

    ```js

    ```

## Structure

- Directory structure
    
    ```
    blog
    ├── source/
    │   ├── _data
    │   │     └── next.yml
    │   └── _posts
    │         └── hello-world.md
    ├── scaffolds/
    │   ├── draft.md
    │   ├── page.md
    │   └── post.md
    ├── public/
    ├── node_modules/
    ├── themes/
    │   └── landscape/
    │         └── _config.yml
    │
    ├── package.json
    └── _config.yml
    ```

