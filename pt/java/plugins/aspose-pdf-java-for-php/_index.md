---
title: Aspose.PDF Java para PHP
linktitle: Aspose.PDF Java para PHP
type: docs
weight: 50
url: /java/aspose-pdf-java-for-php/
description: Aprenda como integrar Aspose.PDF para Java em projetos PHP. Desbloqueie funcionalidades avançadas de PDF para seus aplicativos da web.
lastmod: "2026-06-09"
---
## Introdução ao Aspose.PDF Java para PHP

### Ponte PHP/Java

O PHP/Java Bridge é uma implementação de um [protocolo de rede](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT) de streaming baseado em XML, que pode ser usado para conectar um mecanismo de script nativo, por exemplo PHP, Scheme ou Python, a uma máquina virtual Java. É até 50 vezes mais rápido que o RPC local via SOAP e requer menos recursos do lado do servidor web. É [mais rápido](http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance) e mais confiável do que a comunicação direta por meio da interface nativa Java e não requer componentes adicionais para invocar procedimentos Java de PHP ou procedimentos PHP de Java.

Leia mais em [sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)

### Aspose.PDF para Java

Aspose.PDF for Java é um componente de criação de documentos PDF que permite que seus aplicativos Java leiam, escrevam e manipulem documentos PDF sem usar o Adobe Acrobat.

Aspose.PDF para Java é um componente de preço acessível que oferece uma riqueza incrível de recursos, incluindo: opções de compactação de PDF, criação e manipulação de tabelas, suporte gráfico, funções de imagem, ampla funcionalidade de hiperlink, controles de segurança estendidos e manipulação de fontes personalizadas.

Aspose.PDF para Java permite que você crie arquivos PDF diretamente por meio da API fornecida e dos modelos XML. Usar Aspose.PDF para Java também permitirá que você adicione recursos de PDF aos seus aplicativos rapidamente.

### Aspose.PDF Java para PHP

O projeto Aspose.PDF para PHP mostra como diferentes tarefas podem ser executadas usando APIs Java Aspose.PDF em PHP. Este projeto tem como objetivo fornecer exemplos úteis para desenvolvedores PHP que desejam utilizar Aspose.PDF para Java em seus projetos PHP usando [PHP/Java Bridge](http://php-java-bridge.sourceforge.net/pjb/).

## Requisitos do sistema e plataformas suportadas

### Requisitos do sistema

A seguir estão os requisitos do sistema para usar Aspose.PDF para PHP via Java:

- Tomcat Server 8.0 ou superior instalado.
- PHP/JavaBridge está configurado.
- FastCGI está instalado.
- Componente Aspose.PDF baixado.

### Plataformas Suportadas

A seguir estão as plataformas suportadas:

- PHP 5.3 ou superior
- Java 1.8 ou superior

## Baixar e configurar

### Baixe as bibliotecas necessárias

Baixe as bibliotecas necessárias mencionadas abaixo. Estes são os necessários para executar exemplos Aspose.PDF Java para PHP.

- **Aspose:** [Aspose.PDF para componente Java](https://downloads.aspose.com/pdf/java)
- Ponte PHP/Java

### Baixe exemplos de sites de codificação social

As seguintes versões de exemplos em execução estão disponíveis para download nos sites de codificação social mencionados abaixo:

### GitHub

- Exemplos de Aspose.PDF Java para PHP
  - [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### Como configurar o código fonte na plataforma Linux

Siga estas etapas simples para abrir e estender o código-fonte ao usar:

### 1. Instale o servidor Tomcat

Para instalar o servidor Tomcat, emita o seguinte comando no console Linux. Isso instalará o servidor Tomcat com êxito.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. Baixe e configure PHP/JavaBridge

Para baixar os binários PHP/JavaBridge, emita o seguinte comando no console Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Descompacte os binários PHP/JavaBridge emitindo o seguinte comando no console Linux.

{{< highlight actionscript3 >}}

  descompacte -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Isso extrairá o arquivo **JavaBridge.war**. Copie-o para a pasta tomcat88 **webapps**Â emitindo o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

Ao copiar, o Tomcat8 criará automaticamente uma nova pasta "**JavaBridge**" em **webapps**.

Se alguma mensagem de erro aparecer, instale o **FastCGI** emitindo o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Se o erro **JAVA_HOME** for exibido, abra o arquivo /etc/default/tomcat8 e remova o comentário da linha que define o arquivo JAVA_HOME.

### 3. Configure Aspose.PDF Java para exemplos de PHP

Clone exemplos de PHP emitindo os seguintes comandos dentro da pasta webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### Como configurar o código-fonte na plataforma Windows

Siga as etapas simples abaixo para configurar o PHP/Java Bridge na plataforma Windows

1. Instale o PHP5 e configure normalmente
2. Instale o JRE 6 (Java Runtime Environment) se ainda não o tiver. Você pode verificar isso em C:\Program Arquivos etc. Você pode baixá-lo aqui . Estou usando o JRE 6 porque é compatível com PHP Java Bridge (PJB).

3. Instale o Apache Tomcat 8.0. Você pode baixá-lo aqui

4. Baixe [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copie este arquivo para o diretório webapps do Tomcat.
(ex: C:\Program Arquivos\Apache Software Foundation\Tomcat 8.0\webapps )

5. Reinicie o serviço Apache do Tomcat.

6. Vá para http://localhost:8080/JavaBridge/test.php para verificar se o php funciona. Você pode encontrar outros exemplos lá

7. Copie seu arquivo jar [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) para C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

8. Clone [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) exemplos dentro da pasta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

9. Copie a pasta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java para sua pasta de exemplos Aspose.PDF Java para PHP.

10. Reinicie o serviço Apache Tomcat e comece a usar exemplos.

## Apoie, Estenda e Contribua

### Apoiar

Desde os primeiros dias da Aspose, sabíamos que apenas oferecer bons produtos aos nossos clientes não seria suficiente. Também precisávamos prestar um bom serviço. Nós mesmos somos desenvolvedores e entendemos como é frustrante quando um problema técnico ou uma peculiaridade no software impede você de fazer o que precisa. Estamos aqui para resolver problemas e não para criá-los.

É por isso que oferecemos suporte gratuito. Qualquer pessoa que utilize nosso produto, seja ele comprado ou em avaliação, merece toda nossa atenção e respeito.

Você pode registrar quaisquer problemas ou sugestões relacionadas ao Aspose.Cells Java for PHP usando qualquer uma das seguintes plataformas:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Estenda e contribua

Aspose.PDF Java para PHP é de código aberto e seu código-fonte está disponível nos principais sites de codificação social listados abaixo. Os desenvolvedores são incentivados a baixar o código-fonte e contribuir sugerindo ou adicionando novos recursos ou melhorando os existentes, para que outros também possam se beneficiar dele.

### Código Fonte

Você pode obter o código-fonte mais recente em um dos seguintes locais

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)
