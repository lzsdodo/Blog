# HEXO BLOG
---

## Install

- Install Yarn and Hexo

    ```bash
    brew install yarn
    yarn global add hexo-cli
    ```

- Init blog by Hexo

    ```bash
    cd blog
    hexo init
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

    ```bash
    # Add spaces between CJK characters and western characters.
    hexo-filter-auto-spacing
    ```

## Main config

- Theme: NexT

    ```bash
    git clone https://github.com/theme-next/hexo-theme-next themes/next
    ```

    ```
    theme: next
    ```

- Git auto-deploy: `hexo-deployer-git`

    ```
    deploy:
      type: git
      repo: https://github.com/lzsdodo/blog
      branch: hexo-dev
      message: "Site updated: {{now('YYYY-MM-DD HH:mm:ss') }})"
    ```

- 文章链接唯一化: `hexo-abbrlink` 

    ```
    permalink: posts/:abbrlink/
    abbrlink:
      alg: crc16
      rep: hex
    ```

- markdown 渲染引擎
    - `hexo-renderer-marked`

    ```
    marked:
      gfm: true
      pedantic: false
      sanitize: false
      tables: true
      breaks: true
      smartLists: true
      smartypants: true
    ```

- 页面文章篇数
    - `hexo-generator-index`, `hexo-generator-archive`, `hexo-generator-category`, `hexo-generator-tag`

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

- Sitemap: `hexo-generator-seo-friendly-sitemap`

    ```
    sitemap:
      path: sitemap.xml
    ```

## Theme Config

- Basic Config: `vi /blog/themes/next/_config.yml`

    ```
    scheme: Mist                    # Scheme 主题
    highlight_theme: night bright   # Code Highlight 代码高亮
    ```


- 页面文章篇数

    ```
    index_generator:
      per_page: 5

    archive_generator:
      per_page: 20
      yearly: true
      monthly: true

    tag_generator:
      per_page: 10
    ```

## Structure

- Directory structure
    
    ```
    blog
    ├── source/
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

