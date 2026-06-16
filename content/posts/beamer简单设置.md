---
title: beamer简单设置
date: '2024-12-03T22:26:11+08:00'
categories:
- 便利贴
---


简单的beamer设置

```tex
\documentclass{beamer}

\usepackage[UTF8]{ctex}

\usetheme{Madrid}
% \usefonttheme[onlymath]{serif}
\usefonttheme{serif}

\usepackage[T1]{fontenc}
\usepackage{palatino}
\usepackage{mathrsfs}
\usepackage{calligra}
\usepackage{bm}

\usepackage{amsmath,amsthm,amsfonts,amssymb}

\usepackage{extarrows}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{multicol}

\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=,
    filecolor=blue,
    urlcolor=blue,
    citecolor=cyan,
}

\usepackage{graphicx}
\graphicspath{
    {./figure/}{./figures/}{./image/}{./images/}{./graphic/}{./graphics/}{./picture/}{./pictures/}
}
\usepackage{subcaption}

\title{科学作为天职}
\author{宝多六十花}
\date{2024.12.03}

\begin{document}

\maketitle

\end{document}
```

---

最近老做梦。