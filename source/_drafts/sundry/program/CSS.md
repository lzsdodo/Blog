- 学习途径：慕课网《HTML+CSS基础课程》    
- Summarized by Zachary 

---    
## 1  学习CSS，为网页添加样式    
### 1.1 认识CSS    
>    *CSS全称为“层叠样式表 (Cascading Style Sheets)”，    
它主要是用于定义HTML内容在浏览器内的显示样式，如文字大小、颜色、字体加粗等。*   

    <style type="text/css">    
    p{    
        font-size:12px;     
        /* 设置文字字号 */      
        color:red;
        /* 设置文字颜色 */     
        font-weight:bold;
        /* 设置字体加粗 */     
    }    
    </style>    
   
1. 文本用 `<span>...</span>` 括起来。    
2. 用 `span{ color:red; }` 设定文本样式。    
3. 注释代码：CSS中用 `/*注释文本*/` 。    

### 1.2 CSS代码语法       
![CSS代码语法](http://upload-images.jianshu.io/upload_images/80247-0646a2e89eb49654.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)    

- **语法：css 样式由选择符和声明组成，而声明又由属性和值组成。**     

1. 选择符：又称选择器，指明网页中要应用样式规则的元素。 
2. 声明：大括号 `｛｝` 中的就是声明，属性和值之间用英文冒号 `：` 分隔。当有多条声明时，中间可以英文分号 `;` 分隔。    

---        
## 2  CSS样式基本知识    
>    *CSS 样式代码插入的形式来看基本可以分为以下3种：**内联式、嵌入式和外部式**三种。*     
 
### 2.1 内联式css样式，直接写在现有的HTML标签中    
- 内联式css样式，直接写在在HTML标签中，同时css样式代码写在 `style=""` 双引号中，如果有多条css样式代码设置可以写在一起，中间用分号 `;` 隔开。    
    例：    
    `<p style="color:red">这里文字是红色。</p>`    

### 2.2 嵌入式css样式，写在当前的文件中    
- 嵌入式css样式，就是把css样式代码写在 `<style type="text/css"></style>` 标签之间。        
注意：嵌入式css样式必须写在 `<style></style>` 之间，并且一般情况下嵌入式css样式写在 `<head></head>` 之间。    
    例：
    
        <style type="text/css">
        span{
            color:red;
        }
        </style>
    
### 2.3 外部式css样式，写在单独的一个文件中    
- 外部式css样式，把 css 代码写进单独的外部文件中，文件以“.css”为扩展名，在 head 标签内（不是在 style 标签内）使用 link 标签将 css 样式文件链接到HTML文件内。    
    例：    
    `<link href="base.css" rel="stylesheet" type="text/css" />
` 
  
        span{
            color:red;
            font-size:20px;
        } 
    注意：    
    1. css样式文件名称以有意义的英文字母命名，如 **main.css**。    
    2. **rel="stylesheet" type="text/css"** 是固定写法不可修改。    
    3. link 标签位置一般写在 head 标签之内。    
    
### 2.4 三种方法的优先级    
- 优先级：**权值相同**的条件下，遵循的是**就近原则（离被设置元素越近优先级别越高）。**    
    一般情况：**内联式 > 嵌入式 > 外部式**（因为一般 style 标签写在 link 标签后边）。    

---    
## 3 CSS选择器    
### 3.1 什么是选择器    
> 每一条css样式声明（定义）由两部分组成。    

        选择器{
            样式;
        }    

- 注意：在 `{}` 之前的部分就是“选择器”，“选择器”指明了 `{}` 中的“样式”的作用对象，也就是“样式”作用于网页中的哪些元素。      

### 3.2 选择器    
1. **标签选择器**，就是html代码中的标签。    
    如 `<html>`、`<body>`、`<h1>`、`<p>`、`<img>` 等等。
2. **类选择器**，是在css样式编码中是最常用到的。    
    **语法：`.类选器名称{css样式代码;}`**     
    1. 使用合适的标签把要修饰的内容标记起来。    
    2. 使用 `class="类选择器名称"` 为标签设置一个类。     
    3. style 标签内 设置类选器 css样式。      
    *注意：英文圆点 `.` 开头，同时类选器名称可任意起名（不能中文）。*    
    例：    


            1+2.
            <span class="stress">修饰的内容</span>
            3.
            .stress{
                color:red;
            }
            /* 类前面要加入一个英文圆点 */      
            
3. **ID选择器**，很多方面ID选择器都类似于类选择符，但也有一些重要的区别。    
    1. 为标签设置 `id="ID名称"`，而不是 `class="类名称"`。    
    2. ID选择符的前面是 `#` 号，而不是英文圆点 `.`。    
 
4. **类和ID选择器的区别**        
    1. 相同点：    
        - 可以应用于任何元素。    
    2. 不同点：    
        - 一个HTML文档中，ID选择器只能使用一次，而类选择器可以使用多次。    
        - 类选择器，可以使用词列表方法，为一个元素同时设置多个样式，而ID选择器不行（不能使用 ID 词列表）。    
        `<span class="class1 class2">文本</span>` 这个是可以的。    
        `<span id="id1 id2">文本</span>` 这个是错误的。    

5. **子选择器**，用 `>`，选择指定标签元素的第一代子元素。    
    - **语法：`.class1>element1{border:1px solid red;}`**    
    - 效果：使class名为class1下的子元素element1加入红色实线边框。

6. **包含(后代)选择器**，即加入空格,用于选择指定标签元素下的后辈元素。        
    - **语法：`.class1  span{color:red;}`**    
    - 效果：后代选择器是作用于所有子后代元素。后代选择器通过空格来进行选择。    
    - 注意：>作用于元素的第一代后代，空格作用于元素的所有后代。        

7. **通用选择器**，功能最强大的选择器，它使用一个 `*` 号指定，它的作用是匹配html中所有标签元素。
    - `{color:red;}`

8. **伪类选择符**，允许给html不存在的标签（标签的某种状态）设置样式。    
    - `a:hover{color:red;}`    
    - 可以兼容所有浏鉴器的“伪类选择符”就是 a 标签上使用 :hover ，`a:hover`的组合。    
    
9. **分组选择符**，为多个标签元素设置同一个样式时，可以使用分组选择符`","`。    
    - `h1,span{color:red;}`    
    -  相当于对h1、span分别设置。    

---    
## 4 CSS的继承、层叠和特殊性    
### 4.1 继承    
> 允许样式不仅应用于某个特定html标签元素，而且应用于其后代。   
> 但注意有一些css样式是不具有继承性的。如border:1px solid red;    

### 4.2 特殊性    
> 为同一个元素设置了不同的CSS样式代码，浏览器是根据权值来判断使用哪种css样式的，权值高的就使用哪种css样式。    

- 权值的规则：**标签的权值为1，类选择符的权值为10，ID选择符的权值最高为100。**    
- 注意：继承也有权值但很低，有提出说只有0.1，可理解为继承权值最低。    

### 4.3 叠层    
> 层叠就是在html文件中对于同一个元素可以有多个css样式存在，当有相同权重的样式存在时，会根据这些css样式的前后顺序来决定，处于最后面的css样式会被应用。    

- **内联样式表（标签内部）> 嵌入样式表（当前文件中）> 外部样式表（外部文件中）**        

### 4.4 重要性    
- 语法：`p{color:red!important;}`    
- 使用 `!important` 来设置最高权限，而且要写在分号的前面。    

---    
## 5 CSS格式化排版    
### 5.1 文字排版 —— 字体、字号、颜色    
> 使用css样式为网页中的文字设置字体、字号、颜色等样式属性。    

- 语法：
- 字体：`body{font-family:"宋体";}`      
- 字号、颜色：`body{font-size:12px;color:#666}`   
- 例子：
- 修改字体为“微软雅黑” `body{font-family:"Microsoft Yahei";}`    
- 设置网页中文字的字号为12像素，并把字体颜色设置为#666(灰色)。      

### 5.2 文字排版 —— 粗体、斜体、下划线、删除线         
- 语法： 
- 粗体：`p a{font-weight:bold;}`    
- 斜体：`p a{font-style:italic;}`  
- 下划线：`p a{text-decoration:underline;}`  
- 删除线：`p a{text-decoration:line-through;}`  
 
### 5.3 段落排版 —— 缩进、行间距（行高）、字母间距、字间距、对齐    
> 注意：2em为文字2倍大小。    
> 块状元素中的文本、图片设置样式。    

- 语法：
- 缩进：`p{text-indent:2em;}`  
- 行间距：`p{line-height:2em;}`  
- 字母间距、字间距： 

        h1{ 
            letter-spacing:50px;    
            /* 字母与字母之间间距 */    
            word-spacing:50px;  
            /* 单词与单词之间间距 */
            text-align:center;  
            /* 居中 */ 
            text-align:left;    
            /* 左对齐 */    
            text-align:right;   
            /* 右对齐 */
        }   

---     

## 6 CSS盒模型   
### 6.1 元素分类    
> html中的标签元素大体被分为三种不同的类型：   
> **块状元素**、**内联元素**(又叫行内元素)和**内联块状元素**。  

- 常用的块状元素：

        <div>、<p>、<h1>...<h6>、<ol>、<ul>、<dl>、
        <table>、<address>、<blockquote>、<form>    
- 常用的内联元素：

        <a>、<span>、<br>、<i>、<em>、<strong>、
        <label>、<q>、<var>、<cite>、<code> 
- 常用的内联块状元素：    
        
        <img>、<input>   
  
### 6.2 元素分类 —— 块级元素    
> html中，`<div>、<p>、<h1>、<form>、<ul>、<li>` 就是块级元素。 
> 内联元素通过代码 `{display:block;}` 将元素显示为块级元素。  

- 特点：   
    1. 每个块级元素都从新一行开始，并且其后元素也另起一行。 
    2. 元素的高度、宽度、行高以及顶和底边距都可设置。  
    3. 元素宽度在不设置的情况下，是它本身父容器的100%。   

### 6.3 元素分类 —— 内联元素    
> html中，`<span>、<a>、<label>、<input>、<img>、<strong>、<em>` 就是典型的内联元素(行内元素)(inline)元素。 
> 块状元素可通过代码 `{display:inline;}` 设置为内联元素。  

- 特点：   
    1. 和其他元素都在一行上；  
    2. 元素的高度、宽度、行高及顶部和底部边距**不可**设置； 
    3. 元素的宽度就是它包含的文字或图片的宽度，不可改变。    

### 6.4 元素分类 —— 内联块状元素  
> 内联块状元素就是同时具备内联元素、块状元素的特点。
> 代码 `display:inline-block` 就是将元素设置为内联块状元素。
> `<img>、<input>` 标签就是这种内联块状标签。


### 6.5 盒模型      
1. 内**填充**，称 `padding`; 
2. **边框**，称 `border`;     
3. 外**边界**，称 `margin`;     

- 注意    
    - 内填充、边框、外边界都有四个方向: `-top`、`-right`、`-bottom`、`-left`;  
    - 实际高度 = 元素高度+上下内填充+上下边框+上下边界；实际宽度同理。       
- `<div>`、`<ul>`、`<ol>`、`<p>`、`<h>`、`<table>` 这些***块级标签***，都具备**盒子模型**的特征。   

### 6.6 盒模型 —— 边框       
- 盒子模型的**边框**，绕着**内容**及**补白**，可以设置三个边框属性。   
    1. 粗细   
    2. 样式   
    3. 颜色

- 语法：   

        /* 缩写 */    
        div{    
            border:2px  solid  red; 
        }
        /* 完整写法 */       
        div{    
            border-width:2px;       
            border-style:solid;     
            border-color:red;     
        }   
        /* 单方向设置边框 */          
        div{    
            border-bottom:1px solid red;    
        }        
    
- 常见样式： 
    - border-style（边框样式）: `dashed`、`dotted`、`solid`；（虚线、点线、实线）； 
    - border-color（边框颜色）: `#888`；（十六进制，`#` 不可忽略）    
    - border-width（边框宽度）: `thin`、`medium`、`thick`；（最常用还是像素 `px`）
    - border-bottom、border-top、border-right、border-left：为标签单独设置单个方向的边框。 

### 6.7 盒模型 —— 宽度和高度    
- css定义的宽 `width` 和高 `height`，指的是内容范围。 
- 元素实际宽度（盒子宽度）=左边界+左边框+左填充+内容宽度+右填充+右边框+右边界。    
- `width`、`padding`、`border`、`margin`；
![盒模型-宽度与高度](http://upload-images.jianshu.io/upload_images/80247-e9618c1350db6aaf.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  
![元素盒模型](http://upload-images.jianshu.io/upload_images/80247-7e3ae0b778e089b8.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)  

        /* css代码 */
        div{    
            width:200px;    
            padding:20px;   
            border:1px solid red;   
            margin:10px;    
        }   
        /* 
            元素实际长度为：
            10px+1px+20px+200px+20px+1px+10px=262px。     
        */      
        <!-- html代码 -->
        <body>  
            <div> 文本内容 </div>   
        </body> 

- 补充：块状元素特点之一：不设置宽度情况下，显示为父容器的100%。 

### 6.8 盒模型 —— 填充、边界   
- 元素**内容**与**边框**之间可设置距离，称“**填充(padding)**”。    
- **元素**与**其他元素**之间可设置距离，称“**边界(margin)**”。 
- padding 和 margin 的区别，分别在边框的里侧与外侧。

        /* 单独写 */   
        div{    
           padding-top:20px;    
           padding-right:10px;  
           padding-bottom:15px; 
           padding-left:30px; 
           
           margin-top:20px;    
           margin-right:10px;  
           margin-bottom:15px; 
           margin-left:30px;    
        }   
        /* 都相同 */   
        div{    
            padding:10px;   
            margin:10px;
        }   
        /* 上下，左右分别一样 */    
        div{    
            padding:10px 20px;
            margin:10px 20px;
        }   

--- 

## 7 CSS布局模型    
### 7.1 CSS布局模型     
> **布局模型**与**盒模型**都是CSS*最基本、最核心*的概念。  
> 布局模型是建立在盒模型的基础之上。     
> CSS包含3种基本布局模型，`Flow`、`Layer`、`Float`； 

- 网页中，元素有三种布局模型：    
    1. 流动模型（Flow）；  
    2. 浮动模型（Float）；  
    3. 层模型（Layer）；     

### 7.2 流动模型     
- 网页在默认状态下HTML网页元素都是根据流动模型来分布网页内容的。 

- 流动模型的典型特征： 
    1. **块状元素**都在所处的**包含元素**内，**自上而下**，按顺序垂直延伸分布。   
        - 块状元素，默认宽度100%，所以实际上，它会以**行的形式**占据位置。 
    2. ，**内联元素**都会在所处的包含元素内，**从左到右**，水平分布显示。   
        - `a`、`span`、`em`、`strong` 等标签都是内联元素。   

### 7.3 浮动模型   
- 设置元素浮动可以实现块状元素并排显示。   
- 任何元素默认情况下不能浮动，可通过CSS定义为浮动，如 `div`、`p`、`table`、`img` 等元素。  

        /* 示例1 */   
        div{    
            width:200px;    
            height:200px;   
            border:2px solid red;   
            float:left; 
        }   
        <div id="div1"></div>   
        <div id="div2"></div>   
        
        /* 示例2 */   
        div{    
            width:200px;    
            height:200px;   
            border:2px solid red;   
        }   
        #div1{float:left;}  
        #div2{float:right;}     
![示例1](http://upload-images.jianshu.io/upload_images/80247-405dcac4042f0473.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)    
![示例2](http://upload-images.jianshu.io/upload_images/80247-c43e45a09cd7e412.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)    

### 7.4 层模型     
> 让html元素在网页中精确定位，CSS定义了 `positioning` 属性来支持层布局模型。层模型有三种形式：     
> 1. 绝对定位 `position:absolute;`       
> 2. 相对定位 `position:relative;`       
> 3. 固定定位 `position:fixed;`    
> 具有 `left`、`right`、`top`、`bottom` 方向属性。   

1. 绝对定位 
> `position:absolute`   
> 对相对于其**最接近的一个具有定位属性的父包含块**进行绝对定位。     
> 如果不存在包含块，则相对于 `body` 元素，即相对于浏览器窗口。 

            /* 示例1 */
            div{    
                width:200px;    
                height:200px;   
                border:2px red solid;   
                position:absolute;  
                left:100px; 
                top:50px;   
            }   
            <div id="div1"></div>   
![绝对定位](http://upload-images.jianshu.io/upload_images/80247-f991c31cc88c4431.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)   

2. 相对定位 
> `position:relative`   
> 确定元素在**正常文档流**中的偏移位置。  

    - 先以 `static(float)` 方式生成浮动元素，然后相对于**以前的位置移动**，"l、r、t、b"4个元素确定*方向与幅度*，**偏移前位置保留不动**。  

            /* 示例2 */
            div{    
                width:200px;    
                height:200px;   
                border:2px red solid;   
                position:relative;  
                left:100px; 
                top:50px;   
            }   
            <div id="div1"></div>   
![相对定位](http://upload-images.jianshu.io/upload_images/80247-b9d1f08fe052694d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)   

3. 固定定位 
> `position:fixed`  
> 与绝对定位类似，但相对移动的坐标是**视图***（屏幕内的网页窗口）*。

    - 视图本身是固定的，不随浏览器窗口滚动条滚动而变化，除非在屏幕中移动浏览器窗口屏幕位置或改变显示大小。    
    - 因此固定定位的元素会始终位于浏览器窗口内的某个位置，不会受文档流动影响，与 `background-attachment:fixed;` 属性功能相同。  

            /* 示例 */    
            #div1{  
                width:200px;    
                height:200px;   
                border:2px red solid;   
                position:fixed; 
                left:100px; 
                top:50px;   
            }   

### 7.5 Relative与Absolute组合使用   
> 在元素通过被设置相对浏览器(body)设置定位后 
> 可以相对于其他元素进行定位，但必须遵循下面规范   

1. 参照定位的元素必须是相对定位元素的前辈元素    
2. 参照定位的元素必须加入 `position:relative;` 
3. 定位元素加入 `position:absolute` 便可使用 `top`、`bottom`、`left`、`right`进行偏移定位。     

        <!-- 示例 --> 
        <div id="box1"><!--参照定位的元素-->   
            <div id="box2">相对参照元素进行定位</div><!--相对定位元素-->    
        </div>    
        #box1{  
            width:200px;    
            height:200px;   
            position:relative;  
        }   
        #box2{  
            position:absolute;  
            top:20px;   
            left:30px;  
        }  
        <!-- 这样box2就可以相对于父元素box1定位了 -->     

    - 注意    
        1. `position:relative;` 写在父元素中。    
        2. `position:absolute;` 写在子元素中。  

--- 

## 8 CSS代码缩写，占用更少的带宽    
### 8.1 盒模型代码简写 
> 通常有三种缩写方法     

1. top、right、bottom、left值相同 
2. top、bottom值相同、left、right值相同    
3. left、right的值相同   

- 示例代码  

        /* 示例1：top=right=bottom=left; */    
        margin:10px 10px 10px 10px;         
        margin:10px;    
        /* 示例2：top=bottom; left=right; */    
        margin:10px 20px 10px 20px; 
        margin:10px 20px;   
        /* 示例3：left=right; */    
        margin:10px 20px 30px 20px; 
        margin:10px 20px 30px;  
    
- 注意：`padding`、`border` 缩写方法和 `margin` 是一致的。   

### 8.2 颜色值缩写   
> 颜色css样式也可缩写。  
> 当设置的颜色是16进制的色彩值，若每两位的值相同，可缩写一半。   

- 示例代码： 

        /* 示例1 */
        p{color:#000000;}   
        p{color:#000;}  
        /* 示例2 */
        p{color: #336699;}  
        p{color: #369;}  

### 8.3 字体缩写    
> 网页中字体css样式代码也有自己独特的缩写方式。  

- 示例代码： 

        /* 示例1 */   
        body{   
            font-style:italic;  
            font-variant:small-caps;    
            font-weight:bold;   
            font-size:12px;     
            line-height:1.5em;  
            font-family:"宋体",sans-serif;    
        }
        body{
            font:italic small-caps bold 12px/1.5em "宋体", sans-serif;
        }

- 注意：   
    1. 使用该简写方式，要指定 `font-size` 和 `font-family` 属性，其他属性(如 `font-weight`、`font-style`、`font-varient`、`line-height`)未指定则使用默认值。  
    2. 缩写时 `font-size` 与 `line-height` 中间要加入“/”斜扛。   
    3. 一般情况下，对于英文较少的中文网站，下面缩写代码(只有**字号、行间距、中文字体、英文字体设置**)较常用：
        
            /* 示例2 */    
            body{   
                font:12px/1.5em "宋体", sans-serif;               
            }   

--- 

## 9 单位和值   
### 9.1 颜色值 	
> 网页的颜色设置非常重要，有 `color`（字体颜色）、`background-color`（背景颜色）、`border`（边框颜色）等；     
> 设置颜色的方法也有很多种；     

1. 英文命令颜色   
2. RGB颜色    
3. 十六进制颜色   

- 示例代码：   
    
        /* 英文命令颜色 */
        p{color:red;}   
        /* RGB颜色（0~255/0~100%） */  
        p{color:rgb(133,45,200);}   
        p{color:rgb(20%,33%,25%);}  
        /* 十六进制颜色(普遍使用) */
        p{color:#00ffff;}   

- 配色表：  
![配色表](http://upload-images.jianshu.io/upload_images/80247-55342fb0c35a104c.jpg?imageMogr2/auto-orient/strip)    

### 9.2 长度值 
> 长度单位，常用到 `px`（像素）、`em`、`%` 百分比；       
> 要注意，这三种单位都是相对单位。  

1. 像素   
    - CSS 规范中假设“90px=1英寸”，实际与显示器有关。 
2. em   
    - 即是本元素给定字体的 `font-size` 值。   
    - 当 `font-size` 设置单位也为 `em` 时，计算标准以父元素的 `font-size` 为基础。    
3. 百分比  
    - 类似 `em`，字体长度为本元素字体 `font-size` 值乘以百分比。    

--- 	
## 10 CSS样式设置小技巧    
### 10.1 水平居中设置 —— 行内元素     
> 被设置元素为**行内元素**的*文本、图片等*。  
> 通过给**父元素**设置 `text-align:center` 实现水平居中。  

    <!-- 示例 --> 
    <!-- HTML -->   
    <div class="texCenter">
        我是文本，我想要在父容器中水平居中显示。    
    </div>  
    
    /* CSS */
    <style> 
        div.txtCenter{
            text-align:center;
        }
    </style>

### 10.2 水平居中设置 —— 定宽块状元素  
> 当被设置元素为*块状元素*时用 `text-align:center` 就不起作用。    
> 当满足*定宽*和*块状*两个条件，可通过 `左右margin` 值为 `auto` 实现居中。   

    <!-- 示例 --> 
    <!-- HTML -->       
    <div>
        我是定宽块状元素，哈哈，我要水平居中显示。
    </div>
            
    /* CSS */
    <style>
    div{
        /*为了显示居中效果明显为 div 设置了边框*/
        border:1px solid red;
        /*定宽*/
        width:500px;
        /* margin-left 与 margin-right 设置为 auto */
        margin:20px auto;
    }
    </style>
     
### 10.3 水平居中总结 —— 不定宽块状元素方法       
> 不定宽度的块状元素常有三种方法居中     

1. 加入 `table` 标签    
    1. 为设置的居中元素外面加入一个table标签(包括 `<tbody>`、`<tr>`、`<td>` 等)      
    2. 为table设置 `左右margin居中` (与定宽块状元素一样)
    
            <!-- HTML -->
            <div>
                <!-- 重点加入以下标签 -->
                <table><tbody><tr><td>
                    <ul>
                        <li><a href="#">1</a></li>
                        <li><a href="#">2</a></li>
                        <li><a href="#">3</a></li>
                    </ul>
                </td></tr></tbody></table>
            </div>
    
            /* CSS */
            <style>
                table{
                    /* 设置左右margin为auto */
                    margin:0 auto;
                }
                ul{list-style:none;margin:0;padding:0;}
                li{float:left;display:inline;margin-right:8px;}
            </style>
    
2. 设置块级元素display为inline类型    
> 相比第一种，不用增加无语义标签，简化嵌套深度。   
> 将块状元素display类型改变为inline行内元素，缺少一些功能。   
    1. 设置块级元素的 `display` 为 `inline`类型。  
    2. 使用 `text-align:center;` 实现居中效果。  

            <!-- 示例 --> 
            <!-- HTML -->
            <div>
                <ul>
                    <li><a href="#">1</a></li>
                    <li><a href="#">2</a></li>
                    <li><a href="#">3</a></li>
                </ul>
            </div>
    
            /* CSS */
            <style> 
            .container{
                /* 设置居中 */
                text-align:center;
            }
            .container ul{
                list-style:none;
                margin:0;
                padding:0;
            }
            .container li{
                margin-right:8px;
                /* 设置diaplay:inline; */
                display:inline;
            }
            </style>
    

3. 设置 `position:relative` 和 `left:50%;`     
> 保留块状元素仍以 `display:block;` 形式显示。   
> 不增加无语义标签，不增加嵌套深度。 
> 缺点设置了 `position:relative;`    
    1. 为父元素设置 `float:left;`；    
    2. 为父元素设置 `position:relative;` 和 `left:50%;`       
    3. 为子元素设置 `position:relative;` 和 `left:-50%;`    

            <!-- 示例 --> 
            <!-- HTML -->
            <div>
                <ul>
                    <li><a href="#">1</a></li>
                    <li><a href="#">2</a></li>
                    <li><a href="#">3</a></li>
                </ul>
            </div>
    
            /* CSS */
            <style>
            .container{
                /* 设置父元素 */
                float:left;
                position:relative;
                left:50%
            }

            .container ul{
                list-style:none;
                margin:0;
                padding:0;
                /* 设置子元素 */
                position:relative;
                left:-50%;
            }
            .container li{float:left;display:inline;margin-right:8px;}
            </style>

### 10.4 垂直总结 —— 父元素高度确定的单行文本       
> **父元素高度确定的单行文本**的竖直居中的方法是通过设置父元素的 `height` 和 `line-height` 高度一致来实现的。  

    <!-- 示例 --> 
    <!-- HTML -->
    <div class="container">
        hi,imooc!
    </div>
        
    /* CSS */
    <style>
    .container{
        height:100px;
        line-height:100px;
        background:#999;
    }
    </style>

### 10.5 垂直总结 —— 父元素高度确定的多行文本  
> 父元素高度确定的多行文本、图片、块状元素的竖直居中的方法有两种。  

1. 使用插入 `table` (包括 `tbody`、`tr`、`td`)标签，同时设置 `vertical-align：middle`。      
    - css 中有一个用于竖直居中的属性 `vertical-align`，但这个样式只有在***父元素***为 `td` 或 `th` 时，才会生效。所以又要插入 `table` 标签了。  
    -  `td` 标签默认设置 `vertical-align:middle;`。      

            <!-- 示例 --> 
            <!-- HTML -->
            /* ↓↓↓↓↓↓ 重点 ↓↓↓↓↓↓ */
            <table><tbody><tr><td class="wrap">
            /* ↑↑↑↑↑↑ 重点 ↑↑↑↑↑↑ */
            <div>
                <p>看我是否可以居中。</p>
            </div>
            </td></tr></tbody></table>
                
            /* CSS */
            <style>
                .wrap{height:300px;background:#ccc}
            </style>

2. 在 chrome、firefox 及 IE8 以上的浏览器下可以设置块级元素的 `display` 为 `table-cell`，激活 `vertical-align` 属性，但注意 IE6、7 并不支持这个样式。    

        <!-- 示例 --> 
        <!-- HTML -->
        <div class="container">
            <div>
                <p>看我是否可以居中。</p>
            </div>
        </div>
            
        /* CSS */
        <style>
        .container{
            height:300px;
            background:#ccc;
            /* ↓↓↓↓↓↓ 重点 ↓↓↓↓↓↓ */
            /* IE8以上及Chrome、Firefox */
            display:table-cell;
            vertical-align:middle;
            /* ↑↑↑↑↑↑ 重点 ↑↑↑↑↑↑ */
        }
        </style>
        
### 10.6 隐性改变display类型      
> 有一个有趣的现象就是当为元素设置以下 2 个句之一，           
> 不论之前是什么类型元素，`display:none` 除外：
> > position : absolute     
> > float : left 或 float:right      

> 元素会自动变为以 `display:inline-block` 的方式显示，当然就可以设置元素的 `width` 和 `height` 了且默认宽度不占满父元素。     

> `a标签` 是**行内元素**，所以设置它的 `width` 是 没有效果的，但是设置为 `position:absolute` 以后，就可以了。     

        <!-- 示例 --> 
        <!-- HTML -->
        <div class="container">
            <a href="#" title="">点击进入</a>
        </div>
            
        /* CSS */
        <style>
        .container a{
            /* ↓↓↓↓↓↓ 重点 ↓↓↓↓↓↓ */
            position:absolute;
            /* ↑↑↑↑↑↑ 重点 ↑↑↑↑↑↑ */
            width:200px;
            background:#ccc;
        }
        </style>
