---
title: Aspose.PDF Java para Jython
linktitle: Aspose.PDF Java para Jython
type: docs
weight: 60
url: /java/aspose-pdf-java-for-jython/
description: Combine o poder do Aspose.PDF para Java com Jython. Manipule facilmente arquivos PDF em um ambiente Java baseado em Python.
lastmod: "2026-06-09"
---
## Introdução

### O que é Jython?

Jython é uma implementação Java de Python que combina poder expressivo com clareza. Jython está disponível gratuitamente para uso comercial e não comercial e é distribuído com código-fonte. Jython é complementar ao Java e é especialmente adequado para as seguintes tarefas:

- **Scripting incorporado** – Os programadores Java podem adicionar bibliotecas Jython ao seu sistema para permitir que os usuários finais escrevam scripts simples ou complicados que adicionam funcionalidade ao aplicativo.
- **Experimentação interativa** - Jython fornece um interpretador interativo que pode ser usado para interagir com pacotes Java ou com aplicativos Java em execução. Isso permite que os programadores experimentem e depurem qualquer sistema Java usando Jython.
- **Desenvolvimento rápido de aplicativos** - Os programas Python são normalmente de 2 a 10 vezes mais curtos que o programa Java equivalente. Isso se traduz diretamente no aumento da produtividade do programador. A interação perfeita entre Python e Java permite que os desenvolvedores misturem livremente as duas linguagens durante o desenvolvimento e no envio de produtos.

### Aspose.PDF para Java

Aspose.PDF for Java é um componente de criação de documentos PDF que permite que seus aplicativos Java leiam, escrevam e manipulem documentos PDF sem usar o Adobe Acrobat.

Aspose.PDF para Java é um componente de preço acessível que oferece uma riqueza incrível de recursos, incluindo: opções de compactação de PDF, criação e manipulação de tabelas, suporte gráfico, funções de imagem, ampla funcionalidade de hiperlink, controles de segurança estendidos e manipulação de fontes personalizadas.

Aspose.PDF para Java permite que você crie arquivos PDF diretamente por meio da API fornecida e dos modelos XML. Usar Aspose.PDF para Java também permitirá que você adicione recursos de PDF aos seus aplicativos rapidamente.

### Aspose.PDF Java para Jython

Aspose.PDF Java for Jython é um projeto que demonstra/fornece exemplos de uso da API Aspose.PDF for Java em Jython.

## Requisitos do sistema e plataformas suportadas

### Requisitos do sistema

A seguir estão os requisitos do sistema para usar Aspose.PDF Java para Jython:

- Java 1.5 ou superior instalado
- Componente Aspose.PDF baixado
- Jython 2.7.0

### Plataformas Suportadas

A seguir estão as plataformas suportadas:

- Aspose.PDF 15.4 e superior.
- IDE Java (Eclipse, NetBeans...)

## Baixar instalação e uso

### Baixando

As seguintes versões de exemplos em execução estão disponíveis para download no GitHub:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

Baixe o componente Aspose.PDF para Java:

- [Aspose.PDF para Java](https://downloads.aspose.com/pdf/java)

### Instalando

- Coloque o arquivo jar Aspose.PDF para Java baixado no diretório "lib".
- Substitua "your-lib" pelo nome do arquivo jar baixado no arquivo _*init*_.py.

### Usando

Você pode converter PDF em documento doc usando o seguinte código de exemplo:

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

## Apoie, Estenda e Contribua

### Apoiar

Desde os primeiros dias da Aspose, sabíamos que apenas oferecer bons produtos aos nossos clientes não seria suficiente. Também precisávamos prestar um bom serviço. Nós mesmos somos desenvolvedores e entendemos como é frustrante quando um problema técnico ou uma peculiaridade no software impede você de fazer o que precisa. Estamos aqui para resolver problemas e não para criá-los.

É por isso que oferecemos suporte gratuito. Qualquer pessoa que utilize nosso produto, seja ele comprado ou em avaliação, merece toda nossa atenção e respeito.

Você pode registrar quaisquer problemas ou sugestões relacionadas ao Aspose.PDF Java para Jython usando qualquer uma das seguintes plataformas:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Estenda e contribua

Aspose.PDF Java para Jython é de código aberto e seu código-fonte está disponível nos principais sites de codificação social listados abaixo. Os desenvolvedores são incentivados a baixar o código-fonte e contribuir sugerindo ou adicionando novos recursos ou melhorando os existentes, para que outros também possam se beneficiar dele.

### Código Fonte

Você pode obter o código-fonte mais recente em um dos seguintes locais

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java)
