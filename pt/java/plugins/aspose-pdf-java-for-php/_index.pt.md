---
title: Aspose.PDF Java for PHP
type: docs
weight: 50
url: /java/aspose-pdf-java-for-php/
lastmod: "2021-06-05"
---

## Introdução ao Aspose.PDF Java para PHP

### PHP / Java Bridge

O PHP/Java Bridge é uma implementação de um [protocolo de rede](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT) baseado em XML com streaming, que pode ser usado para conectar um motor de script nativo, por exemplo, PHP, Scheme ou Python, com uma máquina virtual Java. Ele é até 50 vezes mais rápido que RPC local via SOAP e requer menos recursos do lado do servidor web. É [mais rápido](http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance) e mais confiável do que a comunicação direta via Java Native Interface, e não requer componentes adicionais para invocar procedimentos Java a partir de PHP ou procedimentos PHP a partir de Java.

Leia mais em [sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)

### Aspose.PDF para Java

Aspose.PDF para Java é um componente de criação de documentos PDF que permite que suas aplicações Java leiam, escrevam e manipulem documentos PDF sem usar o Adobe Acrobat.

Aspose.PDF para Java é um componente acessível que oferece uma incrível riqueza de funcionalidades, incluindo: opções de compressão de PDF, criação e manipulação de tabelas, suporte a gráficos, funções de imagem, funcionalidade extensa de hiperlink, controles de segurança estendidos e manipulação de fontes personalizadas.

Aspose.PDF para Java permite que você crie arquivos PDF diretamente através da API fornecida e de modelos XML. Usar o Aspose.PDF para Java também permitirá que você adicione capacidades de PDF aos seus aplicativos em pouco tempo.

### Aspose.PDF Java para PHP

O projeto Aspose.PDF para PHP mostra como diferentes tarefas podem ser realizadas usando as APIs Aspose.PDF Java em PHP. Este projeto tem como objetivo fornecer exemplos úteis para Desenvolvedores PHP que desejam utilizar o Aspose.PDF para Java em seus projetos PHP usando [PHP/Java Bridge](http://php-java-bridge.sourceforge.net/pjb/).

## Requisitos de Sistema e Plataformas Suportadas

### Requisitos de Sistema

A seguir estão os requisitos de sistema para usar o Aspose.PDF para PHP via Java:

- Tomcat Server 8.0 ou superior instalado.
- PHP/JavaBridge está configurado.
- FastCGI está instalado.
- Componente Aspose.PDF baixado.

### Plataformas Suportadas

As seguintes são as plataformas suportadas:

- PHP 5.3 ou superior
- Java 1.8 ou superior

## Downloads e Configuração

### Baixar Bibliotecas Necessárias

Baixe as bibliotecas necessárias mencionadas abaixo. Estas são necessárias para executar os exemplos do Aspose.PDF Java para PHP.

- **Aspose:** [Componente Aspose.PDF para Java](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

### Baixar Exemplos de Sites de Codificação Social

As seguintes versões de exemplos em execução estão disponíveis para download nos sites de codificação social mencionados abaixo:

### GitHub

- Exemplos do Aspose.PDF Java para PHP
  - [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### Como configurar o código-fonte na plataforma Linux

Siga estas etapas simples para abrir e estender o código-fonte enquanto usa:

### 1. Instalar o Tomcat Server

Para instalar o servidor Tomcat, emita o seguinte comando no console do Linux. Isso instalará com sucesso o servidor Tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. Baixar e Configurar PHP/JavaBridge

Para baixar os binários do PHP/JavaBridge, emita o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Descompacte os binários do PHP/JavaBridge emitindo o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Isto irá extrair o arquivo **JavaBridge.war**. Copie-o para a pasta **webapps** do tomcat8 emitindo o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

Ao copiar, o tomcat8 criará automaticamente uma nova pasta "**JavaBridge**" em **webapps**.


Se alguma mensagem de erro aparecer, instale **FastCGI** emitindo o seguinte comando no console do Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}


Se o erro **JAVA_HOME** for exibido, abra o arquivo /etc/default/tomcat8 e descomente a linha que define o JAVA_HOME.

### 3. Configurar Aspose.PDF Java para Exemplos em PHP

Clone, exemplos em PHP emitindo os seguintes comandos dentro da pasta webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### Como configurar o código-fonte na Plataforma Windows

Por favor, siga os passos simples abaixo para configurar a PHP/Java Bridge na Plataforma Windows

1. Instale o PHP5 e configure como você normalmente faz
2. Instale o JRE 6 (Java Runtime Environment) se você ainda não o tiver. Você pode verificar isso em C:\Program Files etc. Você pode baixá-lo aqui. Estou usando o JRE 6 pois é compatível com PHP Java Bridge (PJB).

3. Instale o Apache Tomcat 8.0. Você pode baixá-lo aqui.

4. Baixe [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copie este arquivo para o diretório webapps do tomcat. (ex: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

5. Reinicie o serviço apache tomcat.

6. Vá para http://localhost:8080/JavaBridge/test.php para verificar se o PHP funciona. Você pode encontrar outros exemplos lá.

7. Copie seu arquivo jar [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) para C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

8. Clone os exemplos de [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) dentro da pasta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

9. Copie a pasta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java para a sua pasta de exemplos do Aspose.PDF Java para PHP.

10. Reinicie o serviço apache tomcat e comece a usar os exemplos.

## Suporte, Estenda e Contribua

### Suporte

Desde os primeiros dias da Aspose, sabíamos que apenas oferecer aos nossos clientes bons produtos não seria suficiente. Também precisávamos oferecer um bom serviço. Somos desenvolvedores e entendemos como é frustrante quando um problema técnico ou uma peculiaridade no software impede você de fazer o que precisa. Estamos aqui para resolver problemas, não criá-los.

É por isso que oferecemos suporte gratuito. Qualquer pessoa que usa nosso produto, seja ela comprada ou em avaliação, merece nossa total atenção e respeito.

Você pode registrar quaisquer problemas ou sugestões relacionados ao Aspose.Cells Java para PHP usando qualquer uma das seguintes plataformas:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Estender e Contribuir

Aspose.PDF Java para PHP é de código aberto e seu código-fonte está disponível nos principais sites de codificação social listados abaixo.
 Desenvolvedores são incentivados a baixar o código-fonte e contribuir sugerindo ou adicionando novas funcionalidades ou melhorando as existentes, para que outros também possam se beneficiar disso.

### Código-Fonte

Você pode obter o código-fonte mais recente em um dos seguintes locais

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)