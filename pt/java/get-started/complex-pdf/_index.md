---

title: Criando um PDF complexo  
linktitle: Criando um PDF complexo  
type: docs  
weight: 60  
url: /pt/java/complex-pdf-example/  
description: Aspose.PDF para Java permite criar documentos mais complexos que contenham imagens, fragmentos de texto e tabelas em um único documento.  
lastmod: "2021-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---

O exemplo [Hello, World](/pdf/pt/java/hello-world-example/) mostrou passos simples para criar um documento PDF usando Java e Aspose.PDF. Neste artigo, vamos analisar a criação de um documento mais complexo com Java e Aspose.PDF para Java. Como exemplo, usaremos um documento de uma empresa fictícia que opera serviços de ferry de passageiros.  
Nosso documento conterá uma imagem, dois fragmentos de texto (cabeçalho e parágrafo) e uma tabela. Para construir tal documento, usaremos a abordagem baseada em DOM. Você pode ler mais na seção [Noções básicas da API DOM](/pdf/pt/java/basics-of-dom-api/).

Se criarmos um documento do zero, precisamos seguir certos passos:

1. Instanciar um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). Neste passo, criaremos um documento PDF vazio com alguns metadados, mas sem páginas.
1. Adicionar uma [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) ao objeto documento. Agora, nosso documento terá uma página.
1. Adicionar uma [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). É uma operação complexa baseada em ações de baixo nível com operadores PDF.
    - Carregar imagem a partir de um fluxo
    - Adicionar imagem à coleção de Imagens dos Recursos da Página
    - Usando o operador GSave: este operador salva o estado gráfico atual.
    - Criar um objeto [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/).
    - Usando o operador ConcatenateMatrix: define como a imagem deve ser posicionada.
    - Usando o operador Do: este operador desenha a imagem.
    - Usando o operador GRestore: este operador restaura o estado gráfico.

1. Crie um [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para o cabeçalho. Para o cabeçalho, usaremos a fonte Arial com tamanho 24pt e alinhamento centralizado.
1. Adicione o cabeçalho aos [Parágrafos](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) da página.
1. Crie um [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para a descrição. Para a descrição, usaremos a fonte Arial com tamanho 24pt e alinhamento centralizado.
1. Adicione (descrição) aos Parágrafos da página.
1. Crie uma tabela, adicione propriedades à tabela.
1. Adicione (tabela) aos [Parágrafos](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) da página.
1. Salve o documento "Complex.pdf".

```java
package com.aspose.pdf.examples;

/**
 * Exemplo Complexo
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.LocalTime;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.ConcatenateMatrix;
import com.aspose.pdf.operators.Do;
import com.aspose.pdf.operators.GRestore;
import com.aspose.pdf.operators.GSave;

public final class ComplexExample {

    private ComplexExample() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/");

    public static void main(String[] args) throws FileNotFoundException {
        // Inicializa o objeto documento
        Document document = new Document();
        // Adiciona página
        Page page = document.getPages().add();

        // -------------------------------------------------------------
        // Adiciona imagem
        Path imageFileName = Paths.get(_dataDir.toString(),"logo.png");
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(imageFileName.toString()));
        // Adiciona imagem à coleção de Imagens dos Recursos da Página
        page.getResources().getImages().add(imageStream);

        // Usando o operador GSave: este operador salva o estado gráfico atual
        page.getContents().add(new GSave());
        Rectangle _logoPlaceHolder = new Rectangle(20, 730, 120, 830);

        // Cria objeto Matrix
        Matrix matrix = new Matrix(new double[] {
            _logoPlaceHolder.getURX() - _logoPlaceHolder.getLLX(), 0, 0,
            _logoPlaceHolder.getURY() - _logoPlaceHolder.getLLY(),
            _logoPlaceHolder.getLLX(), _logoPlaceHolder.getLLY() });

        // Usando o operador ConcatenateMatrix (concatenar matriz): define como a imagem deve ser posicionada
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Usando o operador Do: este operador desenha a imagem
        page.getContents().add(new Do(ximage.getName()));
        // Usando o operador GRestore: este operador restaura o estado gráfico
        page.getContents().add(new GRestore());

        // -------------------------------------------------------------
        // Adiciona Cabeçalho
        TextFragment header = new TextFragment("Novas rotas de ferry no outono de 2020");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // Adiciona descrição
        String descriptionText = "Os visitantes devem comprar ingressos online e os ingressos são limitados a 5.000 por dia. O serviço de ferry está operando com metade da capacidade e em um horário reduzido. Espere filas.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);


        // Adiciona tabela
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("Sai da Cidade");
        headerRow.getCells().add("Sai da Ilha");

        for (Cell headerRowCell : headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState().setForegroundColor(Color.getWhiteSmoke());
        }

        LocalTime time = LocalTime.of(6,0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time=time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save(Paths.get(_dataDir.toString(), "Complex.pdf").toString());
    }

}
```