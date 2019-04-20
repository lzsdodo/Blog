---
abbrlink: 
title: {{ WordPress }}
categories: nil
tags: [WordPress]
date: {{ 2015-01-01 00:00:00 }}
updated: {{ date }}
---

[TOC]

---

- Summarized by Zachary 
- Continuous Updates 

---		

## 文件目录
- 主题下文件`\theme\***`
	1. 分类目录模板 `category.php`
	2. 作者模板 `author.php`
	3. 评论 `comments.php`
	4. 顶部 `header.php`  
	5. 底部 `footer.php`  
	6. 模板函数 `functions.php`   
	7. 首页模板 `index.php`  
	8. 页面模板 `page.php`  
	9. 搜索框、搜索结果 `searchform.php` & `search.php`    
	10. 边栏 `sidebar.php`   
	11. 文章页面 `single.php`
	12. 标签模板 `tag.php` 
	13. 样式表 `style.css`
	14. 可视化编辑器样式表 `editor-style.css`   

---
 
## 修改个人博客  
### 删除wordpress的评论框
- 路径：`wp-content\themes\XXX\comments.php`  
- 操作：注释 `<p class="nocomments">......</p>`  

### 删除 文章发表日期 
- 路径：`content-single.php`  
- 操作：注释 `<div class="entry-meta">......</div>`  

### 删除 文章中“前一篇、后一篇”
- 路径： `single.php`     
- 操作：注释 `<nav id="nav-single">......</nav>`

### 删除 文章末尾注明      
- 路径：`content-single.php` 
- 操作：注释 `<footer class="entry-meta">......</footer>` 
 
### 删除 自豪地使用WordPress  
- 路径：``wp-content\themes\XXX\footer.php` 
- 操作：修改 `<div id="site-generator">......</div>`   

### 删除 搜索框 
- 路径： `searchform.php` 
- 操作：注释 `该文件内容` 
 
### 删除 首页导航栏   
- 路径：`header.php`
- 操作：注释 `<nav id="access" role="navigation">......</nav>`  

### 修改 导航栏到标题的距离   
- 路径：`style.css`   
- 操作：修改 `#site-description` 中的margin即可。  

### 添加返回顶部按钮        
- 路径：`wp-content\themes\XXX\xxx` ，`wp-content\themes\XXX\images`          
- 操作：xxx 下分别添加以下代码， images下加入图片                
- `style.css`    

		// 返回顶部样式    
		#gotop{
			width:49px;
			height:49px;
			position:fixed;
			bottom:20px;
			right:10px;
			top:auto;
			display:block;
			cursor:pointer;
			background: url(myimages/top.gif) no-repeat
		}
		*html #gotop{
			position:absolute;
			bottom:auto; top:expression(eval(document.documentElement.scrollTop+document.documentElement.clientHeight-this.offsetHeight-(parseInt(this.currentStyle.marginTop,10)||0)-(parseInt(this.currentStyle.marginBottom,10)||0)));
		}
		// 返回顶部样式结束

- `footer.php`    

		<!-- 返回顶部 -->
		<div style="display: none;" id="gotop"></div>
		<script type='text/javascript'>
			backTop=function (btnId){
			var btn=document.getElementById(btnId);
			var d=document.documentElement;
			var b=document.body;
			window.onscroll=set;
			btn.onclick=function (){
					btn.style.display="none";
					window.onscroll=null;
					this.timer=setInterval(function(){
						d.scrollTop-=Math.ceil((d.scrollTop+b.scrollTop)*0.1);
						b.scrollTop-=Math.ceil((d.scrollTop+b.scrollTop)*0.1);
					if((d.scrollTop+b.scrollTop)==0) clearInterval(btn.timer,window.onscroll=set);
				},10);
			};
			function set(){btn.style.display=(d.scrollTop+b.scrollTop>100)?'block':"none"}
		};
		backTop('gotop');
		</script>
		<!-- 返回顶部END -->

### WP提速       
1. 取消谷歌Open sans字体加载   
	- 路径：`/wp-includes/script-loader.php`		
	- 操作： 注释语句 `//fonts.googleapis.com/…` 或替换成 `fonts.useso.com`       
2. 数据库缓存文件负担   
	- 删除修订版本，不让修订版本添加到数据中心。   
	- 路径：`wp-config.php`     
	- 操作：添加 `define('WP_POST_REVISIONS', false);`   
3. 清理HEAD头部多余脚本       
	- 路径：`\wp-content\themes\twentyfifteen\functions.php` 
	- 操作：添加以下脚本     

			remove_action( 'wp_head', 'feed_links_extra', 3 ); //去除评论feed
			remove_action( 'wp_head', 'feed_links', 2 ); //去除文章feed
			remove_action( 'wp_head', 'rsd_link' ); //针对Blog的远程离线编辑器接口
			remove_action( 'wp_head', 'wlwmanifest_link' ); //Windows Live Writer接口
			remove_action( 'wp_head', 'index_rel_link' ); //移除当前页面的索引
			remove_action( 'wp_head', 'parent_post_rel_link', 10, 0 ); //移除后面文章的url
			remove_action( 'wp_head', 'start_post_rel_link', 10, 0 ); //移除最开始文章的url
			remove_action( 'wp_head', 'wp_shortlink_wp_head', 10, 0 );//自动生成的短链接
			remove_action( 'wp_head', 'adjacent_posts_rel_link', 10, 0 ); ///移除相邻文章的url
			remove_action( 'wp_head', 'wp_generator' ); // 移除版本号

---   

## 插件  
### 安装插件 
1. 您可以使用插件浏览/安装器查找并安装新插件。  
2. 浏览 WordPress 插件目录来手动安装插件。   
3. 如需手动安装插件，请把插件文件上传至 /wp-content/plugins 目录，然后在此启用。   

###安装插件获得所需填写的主机名(SAE)      
- 主机名：`w.rdc.sae.sina.com.cn`    
- 端口：`3307`      
- 查看方法	
	1. 进入应用管理          
	2. 点击服务管理 -> MYSQL      
	3. 点击数据库操作 -> 管理MYSQL       
	4. MYSQL管理页面顶部可查看主机地址及数据库名。

### 插件们 
1. Markdown 语法支持   
	- [Jetpack 3.6.1](https://wordpress.org/plugins/jetpack/)，（markdown-on-save.1.2.1 已停止更新并入jetpack ）      
2. 代码高亮        
	- [Crayon Syntax Highlighter 2.7.1](https://wordpress.org/plugins/crayon-syntax-highlighter/)（与Jetpack完全兼容）     
	- 设置中不要勾选“捕获 `反引号` 为 标签”，以防和Jetpack插件冲突。         
3. 拦截垃圾评论   
	- [Akismet 3.1.3](https://wordpress.org/plugins/akismet/)      
4. 数据备份        
	- [WordPress Database Backup 2.3.0](https://wordpress.org/plugins/wp-db-backup/)  
5. WordPress移动主题插件   
	- [Wptouch Mobile Plugin v3.34汉化版](https://wordpress.org/plugins/wptouch/)
6. 音乐播放插件   
	- [wp-player](https://wordpress.org/plugins/wp-player/)
	- 完美支持 IE6+，FireFox，Chrome 等现代浏览器，将调用虾米网专辑歌曲至WordPress   
7. 文章阅读次数统计插件   
	- [wp-postviews](https://wordpress.org/plugins/wp-postviews/)   
8. 缓存提速插件（需要写入权限 SAE无法使用）   
	- [wp-super-cache](https://wordpress.org/plugins/wp-super-cache/)   
9. 数据库优化插件   
	- [wp-optimize](https://wordpress.org/plugins/wp-optimize/)   
10.  SEO 插件   
	- [All in One SEO Pack](https://wordpress.org/plugins/all-in-one-seo-pack/)       

---   

## SVN使用教程(基于SAE)

- http://www.cnblogs.com/txw1958/archive/2012/08/27/svn-tutorial.html

---    

## SAE上安装原生WordPress   
### 修改WordPress文件       
1. SAE是没有写权限，添加/修改 `wp-config.php` 文件       
 
		<?php
		/**
		 * WordPress 基础配置文件。
		 *
		 * 本文件包含以下配置选项: MySQL 设置、数据库表名前缀、
		 * 密匙、WordPress 语言设定以及 ABSPATH。如需更多信息，请访问
		 * {@link http://codex.wordpress.org/Editing_wp-config.php 编辑
		 * wp-config.php} Codex 页面。MySQL 设置具体信息请咨询您的空间提供商。
		 *
		 * 这个文件用在于安装程序自动生成 wp-config.php 配置文件，
		 * 您可以手动复制这个文件，并重命名为 wp-config.php，然后输入相关信息。
		 *
		 * @Author Elmer Zhang <freeboy6716@gmail.com>
		 * @package WordPress
		 */
 
		// ** MySQL 设置 - 具体信息来自您正在使用的主机 ** //
		/** WordPress 数据库的名称 */
		define('DB_NAME', SAE_MYSQL_DB);
		/** MySQL 数据库用户名 */
		define('DB_USER', SAE_MYSQL_USER);
		/** MySQL 数据库密码 */
		define('DB_PASSWORD', SAE_MYSQL_PASS);
		/** MySQL 主机 */
		define('DB_HOST', SAE_MYSQL_HOST_M.':'.SAE_MYSQL_PORT);
		/** 创建数据表时默认的文字编码 */
		define('DB_CHARSET', 'utf8');
		/** 数据库整理类型。如不确定请勿更改 */
		define('DB_COLLATE', '');
		define('WP_USE_MULTIPLE_DB', true);
		//请把这里的wordpress修改为你的Storage域名
		/** SAE Storage Domain名称 */
		define('SAE_STORAGE', 'wordpress');
		/** 文件上传路径 */
		define('SAE_DIR', 'saestor://'.SAE_STORAGE.'/uploads');
		define('SAE_URL','http://'.$_SERVER['HTTP_APPNAME'].'-'.SAE_STORAGE.'.stor.sinaapp.com/uploads');

		$db_list = array(
				'write'=> array(
					array(
						'db_host' => SAE_MYSQL_HOST_M.':'.SAE_MYSQL_PORT,
						'db_user'=> SAE_MYSQL_USER,
						'db_password'=> SAE_MYSQL_PASS,
						'db_name'=> SAE_MYSQL_DB,
						'db_charset'=> 'utf8'
						)
					),
				'read'=> array(
					array(
						'db_host' => SAE_MYSQL_HOST_S.':'.SAE_MYSQL_PORT,
						'db_user'=> SAE_MYSQL_USER,
						'db_password'=> SAE_MYSQL_PASS,
						'db_name'=> SAE_MYSQL_DB,
						'db_charset'=> 'utf8'
						)
					),
				);
		$global_db_list = $db_list['write'];
 
		/**#@+
		 * 身份密匙设定。
		 *
		 * 您可以随意写一些字符
		 * 或者直接访问 {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org 私钥生成服务}，
		 * 任何修改都会导致 cookie 失效，所有用户必须重新登录。
		 *
		 * @since 2.6.0
		 */
		define('AUTH_KEY',         hash_hmac('sha1', SAE_ACCESSKEY . 'AUTH_KEY', SAE_SECRETKEY ));
		define('SECURE_AUTH_KEY',  hash_hmac('sha1', SAE_ACCESSKEY . 'SECURE_AUTH_KEY', SAE_SECRETKEY ));
		define('LOGGED_IN_KEY',    hash_hmac('sha1', SAE_ACCESSKEY . 'LOGGED_IN_KEY', SAE_SECRETKEY ));
		define('NONCE_KEY',        hash_hmac('sha1', SAE_ACCESSKEY . 'NONCE_KEY', SAE_SECRETKEY ));
		define('AUTH_SALT',        hash_hmac('sha1', SAE_ACCESSKEY . 'AUTH_SALT', SAE_SECRETKEY ));
		define('SECURE_AUTH_SALT', hash_hmac('sha1', SAE_ACCESSKEY . 'SECURE_AUTH_SALT', SAE_SECRETKEY ));
		define('LOGGED_IN_SALT',   hash_hmac('sha1', SAE_ACCESSKEY . 'LOGGED_IN_SALT', SAE_SECRETKEY ));
		define('NONCE_SALT',       hash_hmac('sha1', SAE_ACCESSKEY . 'NONCE_SALT', SAE_SECRETKEY ));
 
		/**#@-*/
 
		/**
		 * WordPress 数据表前缀。
		 *
		 * 如果您有在同一数据库内安装多个 WordPress 的需求，请为每个 WordPress 设置不同的数据表前缀。
		 * 前缀名只能为数字、字母加下划线。
		 */
		$table_prefix  = 'wp_';
 
		/**
		 * WordPress 语言设置，默认为英语。
		 *
		 * 本项设定能够让 WordPress 显示您需要的语言。
		 * wp-content/languages 内应放置同名的 .mo 语言文件。
		 * 要使用 WordPress 简体中文界面，只需填入 zh_CN。
		 */
		define ('WPLANG', 'zh_CN');
 
		/**
		 * 开发者专用：WordPress 调试模式。
		 *
		 * 将这个值改为“true”，WordPress 将显示所有开发过程中的提示。
		 * 强烈建议插件开发者在开发环境中启用本功能。
		 */
		define('WP_DEBUG', false);
		define('WP_ZH_CN_ICP_NUM', true);
 
		/* 好了！请不要再继续编辑。请保存该文件。 */
 
		/** WordPress 目录的绝对路径。 */
		if ( !defined('ABSPATH') )
			define('ABSPATH', dirname(__FILE__) . '/');
 
		/** 设置 WordPress 变量和包含文件。 */
		require_once(ABSPATH . 'wp-settings.php');
 
2. 根目录新建一个 `config.yaml`   
	- 复制以下内容   
 
			handle: 
				- rewrite:if (!is_file() && !is_dir() && path ~ "^/(.*)") goto "index.php/$1"
 
3. 附件/图片无法上传修正，SAE提供了一个Storage来上传附件，修改 `wp-includes/functions.php` 文件       
	1. 注释掉以下代码：       
 
			$wrapper = null;
 
			//Strip the protocol.
			if( wp_is_stream( $target ) ) {
				 list( $wrapper, $target ) = explode( '://', $target, 2 );
			}
 
			// From php.net/mkdir user contributed notes.
			$target = str_replace( '//', '/', $target );
 
			// Put the wrapper back on the target.
			if( $wrapper !== null ) {
				$target = $wrapper . '://' . $target;
			}
	2. 替换为：   
 
			//For Sina SAE
			if ( substr($target, 0, 10) == 'saestor://' ) {
				return true;
			}
			$target = str_replace( '//', '/', $target );

	3. 在 `$basedir = $dir; $baseurl = $url;` 顶上添加如下代码：       
 
			//For Sina SAE
			$dir = SAE_DIR;
			$url = SAE_URL;

	4. 在 `send_frame_options_header()` 方法上添加以下代码：   
 
			//For Sina SAE
			if ( !function_exists('utf8_encode') ) {
				function utf8_encode($str) {
					$encoding_in = mb_detect_encoding($str);
					return mb_convert_encoding($str, 'UTF-8', $encoding_in);
				}
			}
 
4. 屏蔽WordPress权限检查1，修改 `wp-admin/includes/file.php` 文件   
	- 注释掉以下代码：       
 
			//For Sina SAE
			// Set correct file permissions
			$stat = stat( dirname( $new_file ));
			$perms = $stat['mode'] & 0000666;
			@ chmod( $new_file, $perms );
 
5. 屏蔽WordPress权限检查2，修改 `wp-includes/class-wp-image-editor-gd.php` 文件       
	- 注释掉以下代码：       
 
			//For Sina SAE
			$stat = stat( dirname( $filename ) );
			$perms = $stat['mode'] & 0000666; //same permissions as parent folder, strip off the executable bits
			@ chmod( $filename, $perms );
 
6. 禁用WordPress自动更新，修改 `wp-include/update.php` 文件   
	- 移到底部会发现一大串 `add_action(....)`，保留以下两行代码，其他全部删除   
 
			add_action( 'load-update-core.php', 'wp_version_check' );
			add_action( 'load-update-core.php', 'wp_update_themes' );
 
	- 文件尾部再加入一句   

			add_action( 'load-update-core.php', 'wp_update_plugins' );

### 设置SAE   
1. 登录SAE后点击 `应用` –> `创建新应用` –> 填入`二级域名`、`应用名称`、`应用描述`等信息。           
2. 初始化以下三项：   
	1. `我的应用` –> `服务管理` –> `MySQL` –> `初始化MySQL`       
	2. `Storage` –> `新建一个domain` –> `Domain Name` 输入 `wordpress` –> `创建`           
	3. `Memcache` –> `初始化MC` –> `配额`设为`12M`
3. `代码管理` –> `创建一个版本` -> 输入版本号`1` 并设置为默认版本。           
4. `SVN checkout` 当前应用代码 -> 下载 `wordpress` -> 解压到 `checkout` 的目录下 -> 代码用svn上传并安装。       
5.  安装时候会提醒说没有 `wp-config.php` 这个文件，点击向导中的创建！       
6.  填入安装信息，这里需要注意：   
	1. `mysql` 的 `用户名`：你的应用的 `accesskey`   
	2. `mysql` 的 `密码`：你的应用的 `secretkey`   
	3. `数据库名`：app_应用名       
	4. `主机域名`：`w.rdc.sae.sina.com.cn:3307`
	5. 下一步会提醒没有权限创建 `wp-confing.php` 这个文件，安装提示拷贝那些生成的代码，然后在svn上面创建 `wp-config.php` 这个文件，贴上那些代码保存！   
7. 用svn提交文件，配置后wp进入后台，安装主题、插件，神马的都有！    

---       
