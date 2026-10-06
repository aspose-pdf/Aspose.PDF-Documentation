---
title: Aspose.PDF Java for Jython
linktitle: Aspose.PDF Java for Jython
type: docs
weight: 60
url: /pt/java/aspose-pdf-java-for-jython/
description: Combine o poder do Aspose.PDF for Java com o Jython. Manipule arquivos PDF de forma simples em um ambiente Java baseado em Python.
lastmod: "2026-10-06"
---
## Introdução

### O que é Jython?

Jython é uma implementação Java do Python que combina poder expressivo com clareza. Jython está disponível gratuitamente para uso comercial e não comercial e é distribuído com código-fonte. Jython complementa o Java e é especialmente adequado para as seguintes tarefas:

- **Embedded scripting** - Programadores Java podem adicionar as bibliotecas Jython ao seu sistema para permitir que os usuários finais escrevam scripts simples ou complexos que adicionem funcionalidade ao aplicativo.
- **Experimentação interativa** - Jython fornece um interpretador interativo que pode ser usado para interagir com pacotes Java ou com aplicações Java em execução. Isso permite que os programadores experimentem e depurem qualquer sistema Java usando Jython.
- **Desenvolvimento rápido de aplicativos** - Programas Python são tipicamente de 2 a 10 vezes mais curtos que o programa Java equivalente. Isso se traduz diretamente em maior produtividade dos programadores. A interação perfeita entre Python e Java permite que os desenvolvedores misturem livremente as duas linguagens tanto durante o desenvolvimento quanto na entrega de produtos.

### Aspose.PDF for Java

Aspose.PDF for Java é um componente de criação de documentos PDF que permite que suas aplicações Java leiam, gravem e manipulem documentos PDF sem usar o Adobe Acrobat.

Aspose.PDF for Java é um componente com preço acessível que oferece uma incrível riqueza de recursos, incluindo: opções de compressão de PDF, criação e manipulação de tabelas, suporte a gráficos, funções de imagem, funcionalidade extensiva de hyperlink, controles de segurança avançados e custom Font handling.

Aspose.PDF for Java permite que você crie arquivos PDF diretamente através da API fornecida e dos modelos XML. Usar Aspose.PDF for Java também permitirá que você adicione recursos PDF às suas aplicações em pouco tempo.

### Aspose.PDF Java for Jython

Aspose.PDF Java for Jython é um projeto que demonstra / fornece exemplos de uso da API Aspose.PDF for Java em Jython.

## Requisitos do Sistema e Plataformas Suportadas

### Requisitos do Sistema

A seguir estão os requisitos do sistema para usar Aspose.PDF Java for Jython:

- Java 1.5 ou superior instalado
- Componente Aspose.PDF baixado
- Jython 2.7.0

### Plataformas suportadas

A seguir estão as plataformas suportadas:

- Aspose.PDF 15.4 e superior.
- IDE Java (Eclipse, NetBeans ...)

## Baixar Instalação e Uso

### Baixar

As seguintes versões de exemplos em execução estão disponíveis para download no GitHub:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

Baixar componente Aspose.PDF for Java:

- [Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)

### Instalar

- Coloque o arquivo jar do Aspose.PDF for Java baixado no diretório "lib".
- Substitua "your-lib" pelo nome do arquivo jar baixado no arquivo _*init*_.py.

### Usar

Você pode converter Pdf para documento doc usando o código de exemplo a seguir:

```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'

        # Open the target document
        pdf = Document(dataDir + 'input1.pdf')

        # Save the concatenated output file (the target document)
        pdf.save(dataDir + "output.doc")

        print "Document has been converted successfully"

if __name__ == '__main__':

    PdfToDoc()
```

## Suporte, Expanda e Contribua

### Suporte

Desde os primeiros dias da Aspose, sabíamos que apenas oferecer bons produtos aos nossos clientes não seria suficiente. Também precisávamos fornecer um bom serviço. Somos desenvolvedores nós mesmos e entendemos quão frustrante é quando um problema técnico ou uma peculiaridade no software impede você de fazer o que precisa fazer. Estamos aqui para resolver problemas, não para criá-los.

É por isso que oferecemos suporte gratuito. Qualquer pessoa que usa nosso produto, seja comprando-o ou usando uma avaliação, merece nossa total atenção e respeito.

Você pode registrar quaisquer problemas ou sugestões relacionados a\u0412\u00A0Aspose.PDF Java para Jython usando qualquer uma das plataformas a seguir:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Estenda e Contribua

Aspose.PDF Java para Jython é open source e seu código-fonte está disponível nos principais sites de codificação social listados abaixo. Os desenvolvedores são incentivados a baixar o código-fonte e contribuir sugerindo ou adicionando novos recursos ou aprimorando os existentes, para que outros também possam se beneficiar dele.

### Código-fonte

Você pode obter o código-fonte mais recente a partir de um dos seguintes locais

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java)
