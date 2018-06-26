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

    ```
    yarn add hexo-deployer-git hexo-abbrlink hexo-addlink hexo-renderer-marked hexo-generator-index hexo-generator-archive hexo-generator-category hexo-generator-tag hexo-generator-searchdb 
    hexo-filter-auto-spacing 
    # hexo-generator-seo-friendly-sitemap hexo-pdf
    ```

    ```bash
    # Add spaces between CJK characters and western characters.
    hexo-filter-auto-spacing
    # Hexo tag for embeded pdf
    hexo-pdf
    ```

- Configs
  - When we say **`hexo config`** means the hexo project config
    - PATH: `/hexo/_config.yml`
  - When we say **`themes config`** means the config of theme **`NexT`**. But we want to separate the config from the theme source files, we will fully override default configuration.
    - Original PATH: `/hexo/themes/next/_config.yml`
    - Real PATH: `/hexo/source/_data/next.yml`

## Hexo config

- Git Auto-deploy: `hexo-deployer-git`

    ```
    deploy:
      type: git
      repo: https://github.com/lzsdodo/blog
      branch: hexo-dev
      message: "Site updated: {{now('YYYY-MM-DD HH:mm:ss')}})"
    ```

- 文章链接唯一化: `hexo-abbrlink` 

    ```
    permalink: posts/:abbrlink/
    abbrlink:
      alg: crc32
      rep: hex
    ```

- markdown 渲染引擎: `hexo-renderer-marked`

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
  
  ```
  cd themes/next/
  git clone https://github.com/theme-next/theme-next-fancybox3 source/lib/fancybox
  ```

  ```
  # Real theme config
  fancybox: true
  ```

- `hexo-pdf`: 

  ```
  yarn add hexo-pdf
  ```

  ```
  {% pdf ./bash_freshman.pdf %}
  {% pdf https://drive.google.com/file/d/xxx/preview %}
  {% pdf http://domain.com/example.pdf %}
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

