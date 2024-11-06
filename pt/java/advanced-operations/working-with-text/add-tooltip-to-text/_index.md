---
title: Usando Tooltip 
linktitle: PDF Tooltip
type: docs
weight: 20
url: pt/java/pdf-tooltip/
description: Aprenda como adicionar tooltip ao fragmento de texto em PDF usando Java e Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar Tooltip ao Texto Procurado adicionando Botão Invisível

Freqüentemente é necessário adicionar alguns detalhes para uma frase ou palavra específica como um tooltip no documento PDF para que ele apareça quando o usuário passa o cursor do mouse sobre o texto. Aspose.PDF para Java fornece este recurso para criar tooltips adicionando um botão invisível sobre o texto procurado. O seguinte trecho de código mostrará o caminho para alcançar essa funcionalidade:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.ButtonField;
import com.aspose.pdf.Document;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.TextFragmentAbsorber;
import com.aspose.pdf.TextFragmentCollection;

public class ExampleToolTip {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddToolTip() {
        String outputFile = _dataDir + "Tooltip_out.pdf";

        // Criar documento de exemplo com texto
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("Mova o cursor do mouse aqui para exibir um tooltip"));
        doc.getPages().get_Item(1).getParagraphs().add(new TextFragment("Mova o cursor do mouse aqui para exibir um tooltip muito longo"));
        doc.save(outputFile);

        // Abrir documento com texto
        Document document = new Document(outputFile);
        // Criar objeto TextAbsorber para encontrar todas as frases que correspondem à expressão regular
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("Mova o cursor do mouse aqui para exibir um tooltip");
        // Aceitar o absorvedor para as páginas do documento
        document.getPages().accept(absorber);
        // Obter os fragmentos de texto extraídos
        TextFragmentCollection textFragments = absorber.getTextFragments();

        // Percorrer os fragmentos
        for(TextFragment fragment : textFragments)
        {
            // Criar botão invisível na posição do fragmento de texto
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // Valor de AlternateName será exibido como tooltip por um aplicativo visualizador
            field.setAlternateName ("Tooltip para texto.");
            // Adicionar campo de botão ao documento
            document.getForm().add(field);
        }

        // Próximo será exemplo de tooltip muito longo
        absorber = new TextFragmentAbsorber("Mova o cursor do mouse aqui para exibir um tooltip muito longo");
        document.getPages().accept(absorber);
        textFragments = absorber.getTextFragments();

        for(TextFragment fragment : textFragments)
        {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // Definir texto muito longo
            field.setAlternateName ("Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        // Salvar documento
        document.save(outputFile);
    }
}
```


{{% alert color="primary" %}}

Em relação ao comprimento da dica de ferramenta, o texto da dica de ferramenta é contido no documento PDF como tipo de string PDF, fora do fluxo de conteúdo. Não há restrição efetiva para tais strings em arquivos PDF (veja PDF Reference Appendix C.). No entanto, um leitor em conformidade (por exemplo, Adobe Acrobat) executando em um processador específico e em um ambiente operacional específico tem esse limite. Por favor, consulte a documentação do seu aplicativo leitor de PDF.

{{% /alert %}}

## Criar um Bloco de Texto Oculto e Mostrá-lo ao Passar o Mouse

No Aspose.PDF, um recurso para ocultar ações é implementado pelo qual é possível mostrar/ocultar campo de caixa de texto (ou qualquer outro tipo de anotação) ao passar o mouse sobre algum botão invisível. Para este propósito, a Classe Aspose.Pdf.Annotations.HideAction é usada para atribuir a ação de ocultar/mostrar ao bloco de texto. Por favor, use o seguinte trecho de código para Mostrar/Ocultar um Bloco de Texto ao Passar o Mouse.

Por favor, leve em conta também que as ações PDF nos documentos funcionam bem nos leitores em conformidade (por exemplo.
 Adobe Reader) mas sem garantias para outros leitores de PDF (por exemplo, plugins de navegador web). Fizemos uma breve investigação e descobrimos:

- Todas as implementações da ação de ocultar em documentos PDF funcionam bem no Internet Explorer v.11.0.
- Todas as implementações da ação de ocultar também funcionam no Opera v.12.14, mas notamos algum atraso de resposta na primeira abertura do documento.
- Apenas a implementação usando o construtor HideAction que aceita o nome do campo funciona se o Google Chrome v.61.0 navegar no documento; Por favor, use os construtores correspondentes se a navegação no Google Chrome for significativa:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```java
    public static void name() {
        String outputFile = _dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

        // Criar documento de exemplo com texto
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("Mova o cursor do mouse aqui para exibir o texto flutuante"));
        doc.save(outputFile);

        // Abrir documento com texto
        Document document = new Document(outputFile);
        // Criar objeto TextAbsorber para encontrar todas as frases que correspondem à expressão regular
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("Mova o cursor do mouse aqui para exibir o texto flutuante");
        // Aceitar o absorber para as páginas do documento
        document.getPages().accept(absorber);
        // Obter o primeiro fragmento de texto extraído
        TextFragmentCollection textFragments = absorber.getTextFragments();
        TextFragment fragment = textFragments.get_Item(1);

        // Criar campo de texto oculto para texto flutuante no retângulo especificado da página
        TextBoxField floatingField = new TextBoxField(fragment.getPage(), new Rectangle(100, 700, 220, 740));
        // Definir texto a ser exibido como valor do campo
        floatingField.setValue ("Este é o \"campo de texto flutuante\".");
        // Recomendamos tornar o campo 'somente leitura' para este cenário
        floatingField.setReadOnly(true);

        // Definir a flag 'oculto' para tornar o campo invisível na abertura do documento
        floatingField.setFlags( floatingField.getFlags() | AnnotationFlags.Hidden);

        // Definir um nome de campo único não é necessário, mas permitido
        floatingField.setPartialName ("FloatingField_1");

        // Definir características da aparência do campo não é necessário, mas melhora
        DefaultAppearance da = new DefaultAppearance("Helvetica", 16, java.awt.Color.RED);
        floatingField.setDefaultAppearance(da);
        //new DefaultAppearance("Helv", 10, Color.getBlue()
        floatingField.getCharacteristics().setBackground(Color.getLightBlue());
        floatingField.getCharacteristics().setBorder(Color.getDarkBlue());;
        floatingField.setBorder(new Border(floatingField));
        floatingField.getBorder().setWidth(1);
        floatingField.setMultiline(true);

        // Adicionar campo de texto ao documento
        document.getForm().add(floatingField);

        // Criar botão invisível na posição do fragmento de texto
        Field buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
        // Criar nova ação de ocultar para o campo especificado (anotação) e flag de invisibilidade.
        // (Você também pode referir-se ao campo flutuante pelo nome se o especificou acima.)
        // Adicionar ações de entrada/saída do mouse no campo de botão invisível
        buttonField.getActions().setOnEnter(new HideAction(floatingField, false));
        buttonField.getActions().setOnExit (new HideAction(floatingField));

        // Adicionar campo de botão ao documento
        document.getForm().add(buttonField);

        // Salvar documento
        document.save(outputFile);
    }
```