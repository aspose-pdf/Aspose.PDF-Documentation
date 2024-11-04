---
title: Instalar Aspose.PDF para PHP via Java
linktitle: Instalação
type: docs
weight: 20
url: /php-java/installation/
description: Esta seção mostra uma descrição do produto e instruções para instalar o Aspose.PDF para PHP via Java por conta própria, bem como usando o NuGet.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF para PHP via Java é composto por dois componentes separados: o script wrapper (aspose.pdf.php) e Aspose.PDF para Java. Esses componentes interagem através da Ponte PHP/Java, com cada um exigindo seu próprio ambiente e processo de execução.

## Instalação

1. Instale o Tomcat em qualquer local, como \java\apache-tomcat-9.0.24.
1. Copie JavaBridge.war para a pasta webapps do Tomcat, como \java\apache-tomcat-9.0.24\webapps.
1. Copie aspose-pdf-xx.x.jar para a pasta lib, como \java\apache-tomcat-9.0.24\lib.
1. Execute \bin\startup.bat, JavaBridge.war será implantado em \java\apache-tomcat-9.0.24\webapps\JavaBridge.

1. Teste http://localhost:8080/JavaBridge/test.php para garantir que o PHP está funcionando bem.
1. Copie aspose.pdf.php e example.php para \java\apache-tomcat-9.0.24\webapps\JavaBridge.
1. Abra http://localhost:8080/JavaBridge/example.php ou crie seu próprio arquivo PHP como segue.
Você encontrará a biblioteca Jar e PHP na pasta vendor/aspose/pdf.