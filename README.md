# HEXO BLOG

---

## Install

- Install `Yarn` & `Hexo`

    ```bash
    brew install yarn
    yarn global add hexo-cli
    ```

- Init Hexo & Run

    ```bash
    hexo init blog
    cd blog
    # yarn install
    hexo generate
    hexo server
    hexo deploy
    ```

- Writing

  ```bash
  hexo new draft <title>
  hexo new <layout> <title>
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
    "scripts": {
        "test": "hexo clean && hexo g && gulp && hexo s",
        "publish": "hexo clean && hexo g && gulp && hexo d",
        "build": "hexo generate",
        "clean": "hexo clean",
        "deploy": "hexo deploy",
        "server": "hexo server"
    },
    "dependencies": {
        "hexo": "^5.0.0",
        "hexo-abbrlink": "^2.2.1",
        "hexo-auto-excerpt": "^1.1.2",
        "hexo-deployer-git": "^3.0.0",
        "hexo-filter-auto-spacing": "^0.2.1",
        "hexo-filter-nofollow": "^2.0.2",
        "hexo-footnotes": "^1.0.2",
        "hexo-generator-archive": "^1.0.0",
        "hexo-generator-category": "^1.0.0",
        "hexo-generator-feed": "^3.0.0",
        "hexo-generator-index": "^2.0.0",
        "hexo-generator-searchdb": "^1.3.3",
        "hexo-generator-tag": "^1.0.0",
        "hexo-hide-posts": "^0.1.1",
        "hexo-renderer-ejs": "^1.0.0",
        "hexo-renderer-marked": "^4.0.0",
        "hexo-renderer-stylus": "^2.0.0",
        "hexo-server": "^2.0.0",
        "hexo-simple-image": "^1.0.2",
        "hexo-theme-next": "^8.2.2",
        "hexo-toc": "^1.1.0",
        "hexo-word-counter": "^0.0.3"
    },
    "devDependencies": {
        "gulp": "^4.0.2",
        "gulp-clean-css": "^4.3.0",
        "gulp-htmlclean": "^2.7.22",
        "gulp-htmlmin": "^5.0.1",
        "gulp-imagemin": "^7.1.0",
        "gulp-uglify": "^3.0.2"
    }
    ```

    - Details
        - `hexo-filter-auto-spacing`: Add spaces between CJK characters and western characters.
        - `hexo-pdf`: Hexo tag for embeded pdf

- Configs
    - When we say **`hexo config`** / **`site config`** means the hexo project config
        - PATH: `/hexo/_config.yml`
    - When we say **`themes config`** means the config of theme **`NexT`**. But we want to separate the config from the theme source files, we will fully override default configuration.
        - PATH: `/hexo/_config.next.yml`

## Structure

```bash
hexo
├── _config.yml
├── _config.next.yml
├── gulpfile.js
├── package.json
├── source/
│   ├── robots.txt
│   ├── _data/
│   ├── images/
│   ├── _drafts/
│   └── _posts/
├── scaffolds/
├── node_modules/
├── themes/
│   └── next/
└── public/
```

## Hexo config

> `_config.yml`

- 页面文章篇数: `hexo-generator-index`

    ```yaml
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

- Git 自动部署: `hexo-deployer-git`

    ```yaml
    deploy:
      type: git
      repo: https://github.com/lzsdodo/lzsdodo.github.io
      branch: master
      message: "Blog updated: {{now('MM/DD/YYYY HH:mm:ss')}})"
    ```

- Markdown Support: `hexo-renderer-marked`

    ```yaml
    marked:
      gfm: true
      pedantic: false
      sanitize: false
      tables: true
      breaks: true
      smartLists: true
      smartypants: true
      modifyAnchors: ''
      autolink: true
    ```

- Search: `hexo-generator-searchdb`

    ```yaml
    search:
      path: search.xml
      field: post
      content: true
      format: html
    ```

- RSS: `hexo-generator-feed`

    ```yaml
    feed:
      type: atom
      path: atom.xml
      limit: 20
    ```

- 文章链接唯一化: `hexo-abbrlink`

    ```yaml
    permalink: posts/:abbrlink/
    abbrlink:
      alg: crc32
      rep: hex
    ```

- Table of Content: `hexo-toc`

    ```yaml
    toc:
      maxdepth: 3
      class: toc
      slugify: transliteration
      decodeEntities: false
      anchor:
        position: after
        symbol: '#'
        style: header-anchor
    ```

- Nofollow: `hexo-filter-nofollow`

    ```yaml
    nofollow:
      enable: true
      field: site
      exclude:
        - zsliang.me
      include:
        noreferrer: true
        noopener: true
    ```

- Hide Posts: `hexo-hide-posts`

    ```yaml
    hide-posts:
      filter: hidden
      public_generators: []
      noindex: true
    ```

- Gulp minifier

    ```yaml
    all_minifier: true
    html_minifier:
      enable: true
      ignore_error: false
      silent: false
      exclude:
    css_minifier:
      enable: true
      silent: false
      exclude:
        - '*.min.css'
    js_minifier:
      enable: true
      mangle: true
      silent: false
      output:
      compress:
      exclude:
        - '*.min.js'
    image_minifier:
      enable: true
      interlaced: false
      multipass: false
      optimizationLevel: 2
      pngquant: false
      progressive: false
      silent: false
    ```

- Adding current post link in hexo post page: `hexo-addlink`

  ```yaml
  addlink:
    before_text: hello  # text before the post link
    after_text: bye     # text after the post link
  ```

- Sitemap: `hexo-generator-seo-friendly-sitemap`

    ```yaml
    sitemap:
      path: sitemap.xml
    ```

## Theme Config

- Theme: `NexT`

    ```bash
    git clone https://github.com/theme-next/hexo-theme-next themes/next
    ```

## Optim

- CDN
    - Edit theme config: `source/_data/next.yml`
    - Global: `jsdelivr.com`; CN: `cdn.bootcss.com` / `cdnjs.com`

    ```yaml
    vendors:
      _internal: lib
      jquery: //cdn.jsdelivr.net/npm/jquery@2.1.3/dist/jquery.min.js
      fancybox: //cdn.jsdelivr.net/fancybox/2.1.5/jquery.fancybox.pack.js
      fancybox_css: //cdn.jsdelivr.net/fancybox/2.1.5/jquery.fancybox.min.css
      fastclick: //cdn.jsdelivr.net/npm/fastclick@1.0.6/lib/fastclick.min.js
      velocity: //cdn.jsdelivr.net/npm/velocity-animate@1.5.1/velocity.min.js
      velocity_ui: //cdn.jsdelivr.net/npm/velocity-ui-pack@1.2.2/velocity.ui.min.js
      ua_parser: //cdn.jsdelivr.net/ua-parser.js/0.7.10/ua-parser.min.js
      fontawesome: //cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css
      pace: //cdn.jsdelivr.net/npm/pace-js@1.0.2/pace.min.js
      pace_css: //cdn.jsdelivr.net/npm/pace-js@1.0.2/templates/pace-theme-minimal.tmpl.css
      canvas_nest: //cdn.jsdelivr.net/npm/canvas-nest.js@1.0.0/canvas-nest.min.js
      #...
    ```

- Compress resources files with `gulp`

    - Install

        ```bash
        # Install
        yarn global add gulp-cli
        yarn add -D gulp-clean-css gulp-uglify gulp-htmlmin gulp-htmlclean gulp-imagemin gulp
        ```

    - Config: `gulpfile.js`

        ```js
        /* gulpfile.js on hexo root */

        // Add require
        var gulp      = require('gulp');
        var minifycss = require('gulp-clean-css');
        var uglify    = require('gulp-uglify');
        var htmlmin   = require('gulp-htmlmin');
        var htmlclean = require('gulp-htmlclean');
        var imagemin  = require('gulp-imagemin');

        // Compress public/**/*.html
        gulp.task('minify-html', function() {
          return gulp.src('./public/**/*.html')
            .pipe(htmlclean())
            .pipe(htmlmin({
                 removeComments: true,
                 minifyJS: true,
                 minifyCSS: true,
                 minifyURLs: true,
            }))
            .pipe(gulp.dest('./public'))
        });

        // Compress public/**/*.css
        gulp.task('minify-css', function() {
            return gulp.src('./public/**/*.css')
                .pipe(minifycss())
                .pipe(gulp.dest('./public'));
        });

        // Compress public/**/*.js
        gulp.task('minify-js', function() {
            return gulp.src('./public/**/*.js')
                .pipe(uglify())
                .pipe(gulp.dest('./public'));
        });

        gulp.task('minify-images', function() {
            return gulp.src('./public/images/**/*.*')
                .pipe(imagemin(
                [imagemin.gifsicle({'optimizationLevel': 3}),
                imagemin.jpegtran({'progressive': true}),
                imagemin.optipng({'optimizationLevel': 7}),
                imagemin.svgo()],
                {'verbose': true}))
                .pipe(gulp.dest('./public/images'))
        });

        // Execute gulp task: gulp
        gulp.task('default', [
            'minify-html','minify-css','minify-js','minify-images'
        ]);
        ```

    - Compress before hexo deploy

        ```bash
        hexo clean && hexo generate
        gulp
        hexo server # hexo deploy
        ```

- Simplify hexo command
    - Add scripts to `package.json` and use `yarn run`

    ```json
    {
      //...
      "scripts": {
        "test": "hexo clean && hexo g && gulp && hexo s",
        "publish": "hexo clean && hexo g && gulp && hexo d"
      }
      //...
    }
    ```

    ```bash
    yarn run test
    yarn run publish
    ```
