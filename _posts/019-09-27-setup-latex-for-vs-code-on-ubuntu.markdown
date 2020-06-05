---
layout: post
title: Thiết lập Latex cho VS code trên Ubuntu
date: 2019-09-27 17:00:01 +0530
category: [home, Latex, Ubuntu]
---


<h3>Lựa chọn phiên Texlive complile</h3>

* [Sự khác biệt của phiên bản khác nhau của Texlive](https://tex.stackexchange.com/a/504566/198043)


<h3>Cài đặt</h3>

* Install Texlive Extra:

    `sudo apt install texlive-latex-extra`

* Install VS code

    * `wget -Ovscode.deb https://vscode-update.azurewebsites.net/latest/linux-deb-x64/stable`

    * `sudo dpkg --install vscode.deb`
    * ` sudo apt-get install --force`

<h3>Thiết lập VS Code</h3>

* Cài đặt Latex workshop

    ` code --install-extension James-Yu.latex-workshop`

* Tạo thư mục project latex

    `mkdir latex_project && code latex_project`

    Tạo thư mục `.vscode` trong thư mục gốc của project và tạo file `task.json`

    ```
    {
        "version": "2.0.0",
        "tasks": [
              {
                "label": "Run pdflatex",
                "type": "shell",
                "group": {
                    "kind": "build",
                    "isDefault": true
                },
                "command": "pdflatex",
                "args": [
                    "-interaction=nonstopmode",
                    "-file-line-error",
                    "*.tex"
                ]
            },
            {
                "label": "Run bibtex",
                "type": "shell",
                "group": {
                    "kind": "test",
                    "isDefault": true
                },
                "command": "bibtex",
                "args": [
                    "-terse",
                    "*.aux"
                ]
            }      
        ]
    }
    ```

* Buid: `Ctrl + Shift + B`

