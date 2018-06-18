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
    # Create a new post
    hexo new "New Post"
    # Run Server (localhost:4000)
    hexo server
    # Generate static files
    hexo generate
    # Deploy to remote sites
    hexo deploy 
    # Clean cache files
    hexo clean
    ```

- Plugin

    ```bash
    yarn add <plugin>
    ```

    ```bash
    # Git
    hexo-deployer-git
    # markdown 的渲染引擎
    hexo-renderer-marked
    # 站点地图
    hexo-generator-seo-friendly-sitemap
    # Search
    hexo-generator-search
    ```

- Theme
    - Download
        
        ```bash
        # NexT
        git clone https://github.com/theme-next/hexo-theme-next themes/next
        ```

    - Config

        ```bash
        vi _config.yml
        #theme: next
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
