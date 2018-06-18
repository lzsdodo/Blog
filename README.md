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

    ```bash
    yarn add <plugin>
    ```

    ```bash
    # Git 自动部署
    hexo-deployer-git
    # markdown 渲染引擎
    hexo-renderer-marked
    # 文章链接唯一化
    hexo-abbrlink
    # RSS
    hexo-generator-feed
    # 页面文章篇数
    hexo-generator-index
    hexo-generator-archive
    hexo-generator-tag
    # 文章搜索
    hexo-generator-search
    # 站点地图
    hexo-generator-seo-friendly-sitemap
    ```

## Theme

- Download
    
    ```bash
    # NexT
    git clone https://github.com/theme-next/hexo-theme-next themes/next
    ```

- Basic Config: `vi /blog/themes/next/_config.yml`

    ```
    theme: next
    scheme: Mist
    highlight_theme: night bright

    canvas_nest: true
    ```


- RSS: `hexo-generator-feed`

    ```
    feed:
      type: atom
      path: atom.xml
      limit: 20
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
