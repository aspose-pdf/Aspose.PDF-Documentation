---
title: Instalar Aspose.PDF para Java
linktitle: Instalação
type: docs
weight: 20
url: /pt/java/installation/
description: Esta seção mostra uma descrição do produto e instruções para instalar o Aspose.PDF para Java por conta própria, bem como usando o NuGet.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Componente Aspose.PDF para Java

{{% alert color="primary" %}}

**Aspose.PDF é um componente Java** criado para permitir que desenvolvedores criem documentos PDF, sejam eles simples ou complexos, programaticamente em tempo real. Aspose.PDF para Java permite que os desenvolvedores insiram tabelas, gráficos, imagens, hyperlinks, fontes personalizadas - e mais - em documentos PDF. Além disso, também é possível compactar documentos PDF. Aspose.PDF para Java oferece excelentes recursos de segurança para desenvolver documentos PDF seguros. E a característica mais distinta do Aspose.PDF para Java é que ele suporta a criação de documentos PDF tanto através de uma API quanto a partir de modelos XML.

{{% /alert %}}

## Descrição do Produto


**Aspose.PDF for Java** é implementado usando Java e funciona com JDK 1.8 e superiores. Aspose.PDF for Java pode ser integrado com qualquer aplicação, por exemplo, uma aplicação web JSP/JSF ou uma aplicação Windows.

**Aspose.PDF for Java** é rápido e leve. Ele cria documentos PDF de forma eficiente e ajuda sua aplicação a ter um melhor desempenho. Aspose.PDF for Java é a primeira escolha de nossos clientes ao criar documentos PDF por causa de seu preço, desempenho soberbo e ótimo suporte. Usando esta biblioteca, você pode implementar capacidades ricas para criar arquivos PDF do zero, ou processar completamente documentos PDF existentes sem instalar o Adobe Acrobat.

# Instalação

## Avaliar Aspose.PDF for Java

{{% alert color="primary" %}}

Você pode baixar [Aspose.PDF for Java](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/) para avaliação.
 O download de avaliação é o mesmo que o download adquirido. A versão de avaliação simplesmente se torna licenciada quando você adiciona algumas linhas de código para [aplicar a licença](/pdf/pt/java/licensing/).

{{% /alert %}}

A versão de avaliação do Aspose.PDF oferece toda a funcionalidade do produto, mas possui duas limitações:

- Insere uma marca d'água de avaliação.
- Não mais que quatro elementos de qualquer coleção podem ser visualizados/editados.
- **Um documento mostrando a marca d'água de avaliação**

![Avaliação do Aspose.PDF](evaluate-aspose-pdf_1.png)

{{% alert color="primary" %}}

Se você quiser testar o Aspose.PDF para Java sem as limitações da versão de avaliação, você também pode solicitar uma Licença Temporária de 30 dias. Por favor, consulte [Como obter uma Licença Temporária?](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

## Instalando o Aspose.PDF para Java a partir do Repositório Aspose

A Aspose hospeda todas as APIs Java no [Repositório Aspose](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/). Você pode usar facilmente a API Aspose.PDF para Java diretamente em seus projetos Maven com configurações simples.

### Especificar Configuração do Repositório Aspose

Primeiro, você precisa especificar a configuração/localização do Repositório Aspose no seu Maven pom.xml da seguinte forma:

```xml
 <repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>
```

### Definir Dependência da API Aspose.PDF para Java

Em seguida, defina a dependência da API Aspose.PDF para Java no seu pom.xml da seguinte forma:

```xml
 <dependencies>
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-pdf</artifactId>
        <version>21.7</version>
    </dependency>
</dependencies>
```

Depois de realizar os passos acima, a dependência Aspose.PDF para Java estará finalmente definida no seu projeto Maven.

### Compatibilidade com JDK 11 e Diretrizes de Uso

A API está otimizada para o ambiente Java 11 e todos os testes e funcionalidades funcionam bem. No entanto, para algumas classes, você deve adicionar a dependência externa para adicionar o classpath da classe: javax.xml.bind.annotation.adapters.HexBinaryAdapter, que foi removida do JRE.

Por exemplo:

```xml
<dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.0</version>
</dependency>
```