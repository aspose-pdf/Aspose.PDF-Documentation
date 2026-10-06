---
title: Baixar e configurar o Aspose.PDF em PHP
linktitle: Baixar e configurar o Aspose.PDF em PHP
type: docs
weight: 10
url: /pt/java/download-and-configure-aspose-pdf-in-php/
description: Saiba como baixar e configurar o Aspose.PDF em PHP para fácil integração e manipulação de PDF em seus projetos PHP.
lastmod: "2026-10-06"
---
## Baixar as bibliotecas necessárias

Baixe as bibliotecas necessárias mencionadas abaixo. Estas são necessárias para executar os exemplos do Aspose.PDF Java para PHP.

- **Aspose:** [Componente Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)
- Ponte PHP/Java

## Baixar exemplos de sites de código social

As versões seguintes de exemplos em execução estão disponíveis para download nos sites de codificação social mencionados abaixo:

### GitHub

- **Aspose.PDF Java for PHP Exemplos**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Configurar o código-fonte na plataforma Linux

Por favor, siga estas etapas simples para abrir e expandir o código-fonte ao usar:

## 1. Instalar o servidor Tomcat

Para instalar o servidor Tomcat, execute o comando a seguir no console Linux. Isso instalará com sucesso o servidor Tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. Baixar e configurar PHP/JavaBridge

Para baixar os binários do PHP/JavaBridge, execute o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Descompacte os binários do PHP/JavaBridge emitindo o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Isso extrairá **JavaBridge.war** arquivo. Copie-o para a tomcat88 **webapps** pasta executando o seguinte comando no console Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

Ao copiar, o tomcat8 criará automaticamente uma nova pasta "**JavaBridge**" em **webapps**. Depois que a pasta for criada, verifique se o tomcat8 está em execução e então verifique  http://localhost:8080/JavaBridge  no navegador, deve abrir uma página padrão do JavaBridge.

Se aparecer qualquer mensagem de erro, então instale  **FastCGI** executando o seguinte comando no console Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Após instalar o php5.5 CGI, reinicie o servidor tomcat8 e verifique  http://localhost:8080/JavaBridge  novamente no navegador.

Se **JAVA_HOME** o erro for exibido, então abra o arquivo /etc/default/tomcat8 e descomente a linha que define o JAVA_HOME. Verifique http://localhost:8080/JavaBridge  no navegador novamente, deve vir com a página de Exemplos PHP/JavaBridge.

## 3. Configurar Aspose.PDF Java para PHP exemplos

Clone, exemplos PHP, executando os seguintes comandos dentro da pasta webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

## Configurar o código-fonte no Windows

Por favor, siga os passos simples abaixo para configurar o PHP/Java Bridge na plataforma Windows

1. Instale o PHP5 e configure como normalmente faz.
2. Instale o JRE 6 (Java Runtime Environment) se você donвЂ™t já o possui. Você pode verificar isso em C:\Program Files etc. Você pode baixá-lo aqui . Eu estou usando o JRE 6 pois é compatível com o PHP Java Bridge (PJB).

3. Instale o Apache Tomcat 8.0. Você pode baixá-lo aqui.

4. Baixe JavaBridge.war.
5. Copie este arquivo para o diretório webapps do Tomcat.
(ex: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

6. Reinicie o serviço Apache Tomcat.

7. Acesse http://localhost:8080/JavaBridge/test.php para verificar se o PHP funciona. Você pode encontrar outros exemplos lá

8. Copie seu [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) arquivo jar para C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib.

9. Clonar [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) exemplos dentro da pasta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. Copie a pasta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java para a pasta de exemplos do Aspose.PDF Java for PHP.

11. Reinicie o serviço apache tomcat e comece a usar os exemplos.
