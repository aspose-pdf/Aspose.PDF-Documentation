---
title: Aspose.PDF Java para Jython
type: docs
weight: 60
url: pt/java/aspose-pdf-java-for-jython/
lastmod: "2021-06-05"
---

## Introdução

### O que é Jython?

Jython é uma implementação Java do Python que combina poder expressivo com clareza. Jython está disponível gratuitamente para uso comercial e não comercial e é distribuído com código fonte. Jython é complementar ao Java e é especialmente adequado para as seguintes tarefas:

- **Script embutido** - Programadores Java podem adicionar as bibliotecas Jython ao seu sistema para permitir que os usuários finais escrevam scripts simples ou complicados que adicionem funcionalidade ao aplicativo.
- **Experimentação interativa** - Jython fornece um interpretador interativo que pode ser usado para interagir com pacotes Java ou com aplicativos Java em execução. Isso permite que os programadores experimentem e depurem qualquer sistema Java usando Jython.
- **Desenvolvimento rápido de aplicativos** - Programas Python são tipicamente 2-10X mais curtos do que o programa Java equivalente.
 Isso se traduz diretamente em aumento da produtividade do programador. A interação perfeita entre Python e Java permite que os desenvolvedores misturem livremente as duas linguagens tanto durante o desenvolvimento quanto em produtos finais.

### Aspose.PDF para Java

Aspose.PDF para Java é um componente de criação de documentos PDF que permite que suas aplicações Java leiam, escrevam e manipulem documentos PDF sem usar o Adobe Acrobat.

Aspose.PDF para Java é um componente com preço acessível que oferece uma incrível riqueza de recursos, incluindo: opções de compressão de PDF, criação e manipulação de tabelas, suporte a gráficos, funções de imagem, funcionalidade extensa de hiperlinks, controles de segurança avançados e manipulação de fontes personalizadas.

Aspose.PDF para Java permite que você crie arquivos PDF diretamente através da API fornecida e modelos XML. Usar o Aspose.PDF para Java também permitirá que você adicione capacidades de PDF às suas aplicações em pouco tempo.

### Aspose.PDF Java para Jython

Aspose.PDF Java para Jython é um projeto que demonstra/fornece exemplos de uso da API Aspose.PDF para Java em Jython.
## Requisitos do Sistema e Plataformas Suportadas

### Requisitos do Sistema

A seguir estão os requisitos do sistema para usar o Aspose.PDF Java para Jython:

- Java 1.5 ou superior instalado
- Componente Aspose.PDF baixado
- Jython 2.7.0

### Plataformas Suportadas

A seguir estão as plataformas suportadas:

- Aspose.PDF 15.4 e acima.
- IDE Java (Eclipse, NetBeans ...)

## Download, Instalação e Uso

### Download

As seguintes versões de exemplos em execução estão disponíveis para download no GitHub:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

Baixe o componente Aspose.PDF para Java:

- [Aspose.PDF para Java](https://downloads.aspose.com/pdf/java)

### Instalação

- Coloque o arquivo jar do Aspose.PDF para Java baixado no diretório "lib".
- Substitua "your-lib" pelo nome do arquivo jar baixado no arquivo _*init*_.py.

### Uso

Você pode converter um documento Pdf para doc usando o exemplo de código a seguir:

```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'


        # Abra o documento alvo
        pdf = Document(dataDir + 'input1.pdf')

        # Salve o arquivo de saída concatenado (o documento alvo)
        pdf.save(dataDir + "output.doc")

        print "Documento foi convertido com sucesso"


if __name__ == '__main__':       

    PdfToDoc()
```


## Suporte, Estender e Contribuir

### Suporte

Desde os primeiros dias da Aspose, sabíamos que apenas oferecer bons produtos aos nossos clientes não seria suficiente. Também precisávamos fornecer um bom serviço. Somos desenvolvedores e entendemos como é frustrante quando um problema técnico ou uma peculiaridade no software impede você de fazer o que precisa. Estamos aqui para resolver problemas, não criá-los.

É por isso que oferecemos suporte gratuito. Qualquer pessoa que use nosso produto, seja comprando ou utilizando uma versão de avaliação, merece nossa total atenção e respeito.

Você pode registrar qualquer problema ou sugestão relacionado ao Aspose.PDF Java for Jython usando qualquer uma das seguintes plataformas:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Estender e Contribuir

Aspose.PDF Java for Jython é open source e seu código fonte está disponível nos principais sites de codificação social listados abaixo.
 Desenvolvedores são incentivados a baixar o código-fonte e contribuir sugerindo ou adicionando novas funcionalidades ou melhorando as existentes, para que outros também possam se beneficiar.

### Código-Fonte

Você pode obter o código-fonte mais recente de um dos seguintes locais

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java)