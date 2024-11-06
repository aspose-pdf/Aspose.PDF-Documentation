---
title: O que há de novo
linktitle: O que há de novo
type: docs
weight: 10
url: pt/java/whatsnew/
description: Esta página apresenta as funcionalidades novas mais populares no Aspose.PDF para Java que foram introduzidas em lançamentos recentes.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-06-05"
---

## O que há de novo no Aspose.PDF 24.8

A partir da versão 24.8, suporte para o formato PDF/A-4:

```java

    Document document = new Document(inputPdf);
    // Apenas documentos PDF-2.x podem ser convertidos para PDF/A-4
    document.convert(new ByteArrayOutputStream(), PdfFormat.v_2_0, ConvertErrorAction.Delete);
    boolean converted = document.convert(logFile, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
    document.save(outputFile);
```

Além disso, é possível adicionar texto alternativo para o Selo de Imagem:

A propriedade AlternativeText foi adicionada ao ImageStamp - se um valor for atribuído a ela, então ao adicionar um ImageStamp a um documento, ele terá Texto Alternativo.

```java

    String p1_Alt1 = "*** página 1, Texto alt 1 ***",
                    p1_Alt2 = "*** página 1, Texto alt 2 ***",
                    p2_Alt1 = "--- página 1, Texto alt 1 ---",
                    p2_Alt2 = "--- página 1, Texto alt 2 ---";

    StructTreeRootElement structTreeRoot = document.getTaggedContent().getStructTreeRootElement();

    ImageStamp imageStamp = new ImageStamp(dataDir + "test.jpg");
    imageStamp.setXIndent(100);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setQuality(100);
    imageStamp.setAlternativeText(p1_Alt1);

    // Para a página 1
    document.getPages().get_Item(1).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p1_Alt2);
    document.getPages().get_Item(1).addStamp(imageStamp);

    // Para a página 2
    document.getPages().add();
    imageStamp.setXIndent(400);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setAlternativeText(p2_Alt1);
    document.getPages().get_Item(2).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p2_Alt2);
    document.getPages().get_Item(2).addStamp(imageStamp);

    // Salvar documento
    document.save(outFile);
```


Além disso, o código a seguir mostra como adicionar TextoAlternativo nas imagens existentes em FigureElements.

```java

    String inFile = dataDir + "46040.pdf";
    String outFile = dataDir + "46040_1_out.pdf";

    Document document = new Document(inFile);

    ITaggedContent taggedContent = document.getTaggedContent();
    StructureElement rootElement = taggedContent.getRootElement();

    Iterator tmp0 = (rootElement.getChildElements()).iterator();
    while (tmp0.hasNext())
    {
        com.aspose.pdf.tagged.logicalstructure.elements.Element element = (com.aspose.pdf.tagged.logicalstructure.elements.Element)tmp0.next();
        if (element instanceof com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)
                {
            com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figureElement = (com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)element;

            // Definir Texto Alternativo
            figureElement.setAlternativeText("Texto alternativo da figura (técnica 1)");
        }
    }

    // Salvar documento
    document.save(outFile);
```


## O que há de novo no Aspose.PDF 24.7

Desde o lançamento 24.7, como parte da edição de PDF com tags, foram adicionados métodos no **Aspose.Pdf.LogicalStructure.Element**:

- Tag (adicionar tags a operadores específicos como imagens, texto e links)
- InsertChild
- RemoveChild
- ClearChilds

Esses métodos permitem que você edite tags de arquivos PDF, por exemplo:

```java

    Document document = new Document(dataDir + "test.pdf");

    // Recupere a primeira página do documento.
    Page page = document.getPages().get_Item(1);

    // Inicialize variáveis para segurar elementos BDC (Begin Dictionary Context) para diferentes propósitos.
    BDC imageBdc = null;
    BDC pBdc = null;
    BDC link1Bdc = null;
    BDC link2Bdc = null;
    BDC helloBdc = null;

    // Itere através do conteúdo da página.
    for (int i = 1; i <= page.getContents().size(); i++)
    {
        // Obtenha o operador atual do conteúdo da página.
        Operator op = page.getContents().get_Item(i);

        // Verifique se o operador é uma instância de BDC.
        if (op instanceof BDC) {
        BDC bdc = (BDC)op; // Converta o operador para o tipo BDC.
        if (bdc != null)
        {
            // Verifique se o MCID (Identificador de Conteúdo de Marca) do BDC é 0.
            if (bdc.getProperties().getMCID()[0] != null && bdc.getProperties().getMCID()[0] == 0)
            {
                helloBdc = bdc; // Armazene o BDC para uso posterior.
            }
        }
    }

    // Verifique se o operador é uma instância de Do (Desenhar Objeto).
    if (op instanceof Do) {
        Do doXobj = (Do)op; // Converta o operador para o tipo Do.
        if (doXobj != null)
        {
            // Crie um novo BDC para uma imagem e insira-o no conteúdo da página.
            imageBdc = new BDC("Figure");
            page.getContents().insert(i - 2, imageBdc); // Insira antes do operador atual.
            i++; // Incremente o índice para contabilizar o BDC inserido.
            page.getContents().insert(i + 1, new EMC()); // Insira um EMC (Fim de Conteúdo de Marca).
            i++; // Incremente o índice novamente.
        }
    }

    // Verifique se o operador é uma instância de TextShowOperator (para exibição de texto).
    if (op instanceof TextShowOperator) {
        TextShowOperator tx = (TextShowOperator)op; // Converta o operador para o tipo TextShowOperator.
        if (tx != null)
        {
            // Verifique o conteúdo de texto específico e insira os BDCs correspondentes.
            if (tx.getText().contains("efter Ukendt forfatter er licenseret under"))
            {
                pBdc = new BDC("P");
                page.getContents().insert(i - 1, pBdc); // Insira antes do operador atual.
                i++; // Incremente o índice.
                page.getContents().insert(i + 1, new EMC()); // Insira um EMC.
                i++; // Incremente o índice.
            }
            if (tx.getText().contains("CC"))
            {
                link1Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link1Bdc); // Insira antes do operador atual.
                i++; // Incremente o índice.
                page.getContents().insert(i + 1, new EMC()); // Insira um EMC.
                i++; // Incremente o índice.
            }
            if (tx.getText().contains("Dette billede"))
            {
                link2Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link2Bdc); // Insira antes do operador atual.
                i++; // Incremente o índice.
                page.getContents().insert(i + 1, new EMC()); // Insira um EMC.
                i++; // Incremente o índice.
            }
        }
    }
}
 
    // Recupere o conteúdo com tags do documento.
    ITaggedContent tagged = document.getTaggedContent();

    // Processe o conteúdo com tags para modificar atributos de estrutura.
    // Obtenha o primeiro elemento filho do elemento raiz no conteúdo com tags.
    com.aspose.pdf.tagged.logicalstructure.elements.Element p = tagged.getRootElement().getChildElements().get_Item(1);
    p.clearChilds(); // Limpe os elementos filhos existentes.

    // Marque o helloBdc com o elemento de estrutura pai.
    MCRElement mcr = p.tag(helloBdc);

    // Crie e defina atributos de estrutura para o elemento com tag.
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
            .getAttributes().createAttributes(AttributeOwnerStandard.Layout);
    StructureAttribute attr = new StructureAttribute(AttributeKey.SpaceAfter);
    attr.setNumberValue(30.625); // Defina o atributo de espaço após.
    attrs.setAttribute(attr); // Aplique o atributo à estrutura.

    // Crie um novo FigureElement no conteúdo com tags.
    com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figure = tagged.createFigureElement();
    tagged.getRootElement().insertChild(figure, 2); // Insira o elemento figura na segunda posição.
    figure.setAlternativeText("A fly."); // Defina texto alternativo para a figura.

    // Marque o imageBdc com o elemento figura.
    MCRElement mcr = figure.tag(imageBdc);

    // Recupere o elemento de estrutura pai do MCR (Referência de Conteúdo Marcado) especificado
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Crie um novo StructureAttribute para espaço após o elemento
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(3.625); // Defina o valor do espaço após para 3.625 unidades
    attrs.setAttribute(spaceAfter); // Atribua o atributo de espaço após aos atributos de estrutura

    // Crie um novo StructureAttribute para caixa delimitadora (BBox)
    StructureAttribute bbox = new StructureAttribute(AttributeKey.BBox);
    bbox.setArrayNumberValue(new Double[][] { new Double[] { (71.9971) }, new Double[] { (375.839) }, new Double[] { (523.299) }, new Double[] { (714.345) } });
    // Defina os valores da caixa delimitadora para o atributo de estrutura
    attrs.setAttribute(bbox); // Atribua o atributo de caixa delimitadora aos atributos de estrutura

    // Crie um novo StructureAttribute para posicionamento
    StructureAttribute placement = new StructureAttribute(AttributeKey.Placement);
    placement.setNameValue(AttributeName.Placement_Block); // Defina o tipo de posicionamento como bloco
    attrs.setAttribute(placement); // Atribua o atributo de posicionamento aos atributos de estrutura

    // Recupere o quarto elemento filho do elemento raiz da estrutura com tags
    StructureElement p2 = (StructureElement)tagged.getRootElement().getChildElements().get_Item(3);
    p2.clearChilds(); // Limpe quaisquer elementos filhos existentes de p2

    // Crie um novo SpanElement para ser adicionado a p2
    SpanElement span1 = tagged.createSpanElement();

    // Crie atributos de estrutura para o elemento span
    StructureAttributes attrs = span1.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Crie um novo StructureAttribute para tipo de decoração de texto
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Defina a decoração de texto como sublinhado
    attrs.setAttribute(textDecorationType); // Atribua o atributo de tipo de decoração de texto aos atributos de estrutura

    // Crie um novo StructureAttribute para espessura da decoração de texto
    StructureAttribute textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
    textDecorationThickness.setNumberValue(0); // Defina a espessura da decoração de texto como 0
    attrs.setAttribute(textDecorationThickness); // Atribua o atributo de espessura da decoração de texto aos atributos de estrutura

    // Crie um novo StructureAttribute para cor da decoração de texto
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
    textDecorationColor.setArrayNumberValue(new Double[][] { new Double[] { (0.0196075) }, new Double[] { (0.384308) }, new Double[] { (0.756866) } });
    // Defina os valores de cor RGB para a decoração de texto
    attrs.setAttribute(textDecorationColor); // Atribua o atributo de cor da decoração de texto aos atributos de estrutura

    p2.appendChild(span1); // Anexar o elemento span1 a p2


    // Crie um novo elemento MCR e marque-o com pBdc
    MCRElement mcr = p2.tag(pBdc);
    // Recupere o elemento de estrutura pai do MCR e crie atributos de layout
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Crie um novo StructureAttribute para alinhamento de texto
    StructureAttribute textAlign = new StructureAttribute(AttributeKey.TextAlign);
    textAlign.setNameValue(AttributeName.TextAlign_Center); // Defina o alinhamento de texto como centralizado
    attrs.setAttribute(textAlign); // Atribua o atributo de alinhamento de texto aos atributos de estrutura

    // Crie um novo StructureAttribute para espaço após o elemento
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(21.75); // Defina o valor do espaço após para 21.75 unidades
    attrs.setAttribute(spaceAfter); // Atribua o atributo de espaço após aos atributos de estrutura


    // Crie um novo SpanElement para ser adicionado a p2
    SpanElement span2 = tagged.createSpanElement();

    // Crie atributos de estrutura para o elemento span
    StructureAttributes attrs = span2.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Crie um novo StructureAttribute para tipo de decoração de texto
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Defina a decoração de texto como sublinhado
    attrs.setAttribute(textDecorationType); // Atribua o atributo de tipo de decoração de texto aos atributos de estrutura

    // Crie um novo StructureAttribute para cor da decoração de texto usando a chave especificada.
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);

    // Defina o valor do número do array para o atributo de cor da decoração de texto.
    // A cor é representada em um array de valores RGB, onde cada valor é um Double.
    textDecorationColor.setArrayNumberValue(new Double[][] {
    new Double[] { (0.0196075) }, // Componente vermelho
    new Double[] { (0.384308) },  // Componente verde
    new Double[] { (0.756866) }   // Componente azul
    });

    // Defina o atributo de cor da decoração de texto para o objeto attrs.
    attrs.setAttribute(textDecorationColor);

    // Anexar um elemento span filho ao elemento pai p2.
    p2.appendChild(span2);

    // Crie uma nova instância de LinkElement para o segundo link.
    LinkElement link2 = tagged.createLinkElement();

    // Atribua um ID único ao elemento link usando um UUID gerado aleatoriamente.
    link2.setId(UUID.randomUUID().toString());

    // Anexar o elemento link2 como um filho de span2.
    span2.appendChild(link2);

    // Marque o elemento link2 com a anotação correspondente das anotações da página.
    link2.tag(page.getAnnotations().get_Item(1));

    // Marque o elemento link2 com metadados ou contexto adicional (link2Bdc).
    link2.tag(link2Bdc);

    // Crie outra instância de LinkElement para o primeiro link.
    LinkElement link1 = tagged.createLinkElement();

    // Atribua um ID único ao elemento link1 usando um UUID gerado aleatoriamente.
    link1.setId(UUID.randomUUID().toString());

    // Anexar o elemento link1 como um filho de span1.
    span1.appendChild(link1);

    // Marque o elemento link1 com a anotação correspondente das anotações da página.
    link1.tag(page.getAnnotations().get_Item(2));

    // Marque o elemento link1 com metadados ou contexto adicional (link1Bdc).
    link1.tag(link1Bdc);

    // Remova o primeiro elemento filho do elemento raiz do documento com tags.
    tagged.getRootElement().removeChild(0);

    // Salve o documento no diretório de saída especificado com o nome do arquivo "_out.pdf".
    document.save(dataDir + "_out.pdf");

```


## O que há de novo no Aspose.PDF 24.6

Desde a versão 24.6, o Aspose.PDF para Java permite assinar PDFs com java.security.cert.X509Certificate, java.security.PrivateKey:

Este código recupera um certificado e uma chave privada do armazenamento de certificados e, em seguida, os usa para aplicar uma assinatura digital na primeira página de um documento PDF.

```java

    KeyStore trustStore = KeyStore.getInstance("Windows");
    trustStore.load(null, null);
    java.security.cert.X509Certificate certificate = (java.security.cert.X509Certificate) trustStore.getCertificate("ProfMoriarty");
    PrivateKey key = (PrivateKey) trustStore.getKey("ProfMoriarty", null);

    PdfFileSignature pdfSign = new PdfFileSignature(getInputPdf());
    Signature signature = new ExternalSignature(certificate, key);
    pdfSign.sign(1, "reasonTest", "contactTest", "locationTest", true, new java.awt.Rectangle(1, 691, 100, 100), signature);

    pdfSign.save("PDFJAVA.pdf");
    pdfSign.close();
```

## O que há de novo no Aspose.PDF 24.5

Desde a versão 24.5, os Plugins do Editor de Formulários foram implementados.

**Como Editar Formulários em PDF usando o Editor de Formulários**

- Defina suas chaves de licença
- Crie uma instância da classe FormEditor, que fornece métodos para manipular formulários PDF
- Crie uma instância da classe FormEditorAddOptions, que especifica as opções para adicionar campos de formulário a um documento PDF
- Adicione uma fonte de arquivo de entrada e uma fonte de arquivo de saída ao objeto FormEditorAddOptions, usando a classe FileDataSource, que representa um caminho de arquivo ou fluxo
- Chame o método Process do objeto FormEditor, passando o objeto FormEditorAddOptions como parâmetro
- Acesse o resultado usando ResultContainer.resultCollection

```java

    // Especifique os caminhos de entrada e saída para os arquivos PDF.
    String inputPath = "sample.pdf";
    String outputPath = "out.pdf";

    // Crie uma instância do plugin FormEditor.
    FormEditor pdfFormPlugin = new FormEditor();

    // Crie opções para adicionar campos de formulário.
    ArrayList<FormFieldCreateOptions> options = new ArrayList<FormFieldCreateOptions>();

    // Crie um campo de formulário de caixa de texto.
    FormTextBoxFieldCreateOptions tmp1 = new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 600, 90, 610));
    tmp1.setValue("TextBoxField");
    tmp1.setColor(Color.getChocolate());
    tmp1.setPartialName("TexBoxField");
    options.add(tmp1);

    // Crie um campo de formulário de caixa de combinação.
    FormComboBoxFieldCreateOptions tmp2 = new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 800, 350, 815));

    tmp2.setColor(com.aspose.pdf.Color.getRed());
    tmp2.setEditable(new Boolean[]{true});
    tmp2.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    ArrayList<String> list1 = new ArrayList<String>();
    list1.add("p1");
    list1.add("p2");
    list1.add("p3");
    tmp2.setOptions(list1);
    tmp2.setSelected(new Integer[]{2});
    tmp2.setPartialName("ComboBoxField");
    options.add(tmp2);

    // Crie um campo de formulário de caixa de seleção.
    FormCheckBoxFieldCreateOptions tmp3 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715));
    tmp3.setValue("CheckBoxField 1");
    tmp3.setPartialName("CheckBoxField_1");
    tmp3.setColor(Color.getBlue());
    options.add(tmp3);


    // Crie um campo de formulário de caixa de seleção.
    FormCheckBoxFieldCreateOptions tmp4 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(100, 700, 190, 715));
    tmp4.setChecked(new Boolean[]{true});
    tmp4.setValue("CheckBoxField 2");
    tmp4.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    tmp4.setStyle(new Integer[]{BoxStyle.Cross});
    options.add(tmp4);


    // Crie um campo de formulário de caixa de seleção.
    FormCheckBoxFieldCreateOptions tmp5 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(200, 700, 390, 715));
    tmp5.setPartialName("CheckBoxField_3");
    tmp5.setValue("CheckBoxField 3");
    tmp5.setStyle(new Integer[]{BoxStyle.Star});
    tmp5.setChecked(new Boolean[]{true});
    tmp5.setTextHorizontalAlignment(new HorizontalAlignment[]{HorizontalAlignment.Center});
    options.add(tmp5);

    FormEditorAddOptions opt = new FormEditorAddOptions(options);

    // Adicione arquivos de entrada e saída às opções.
    opt.addInput(new FileDataSource(inputPath));
    opt.addOutput(new FileDataSource(outputPath));

    // Procese os campos de formulário usando o plugin.
    ResultContainer results = pdfFormPlugin.process(opt);
```


Este lançamento nos permite trabalhar com camadas de PDF. Por exemplo:

- bloquear uma camada de PDF
- extrair elementos de camada de PDF
- achatar um PDF com camadas
- mesclar Todas as Camadas dentro do PDF em uma só

**Bloquear uma camada de PDF**

Desde o lançamento 24.5, você pode abrir um PDF, bloquear uma camada específica na primeira página e salvar o documento com as alterações. Foram adicionados dois novos métodos e uma propriedade:

Layer.Lock(); - Bloqueia a camada.
Layer.Unlock(); - Desbloqueia a camada.
Layer.Locked; - Propriedade, indicando o estado de bloqueio da camada.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    Layer layer = page.getLayers().get(0);

    layer.lock();

    document.save(output);
```

**Extrair elementos de camada de PDF**

A biblioteca Aspose.PDF para Java permite extrair cada camada da primeira página e salva cada camada em um arquivo separado.

Para criar um novo PDF a partir de uma camada, o seguinte trecho de código pode ser usado:

```java

    Document document = new Document(inputPath);
    java.util.List<Layer> layers = document.getPages().get_Item(1).getLayers();

    for (Layer layer : layers)
    {
        layer.save(outputPath);
    }
```


**Achatamento de um PDF em camadas**

A biblioteca Aspose.PDF para Java abre um PDF, itera por cada camada na primeira página e achata cada camada, tornando-a permanente na página.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);

    for (Layer layer : page.getLayers())
    {
        layer.flatten(true);
    }
    document.save(output);
```

O método Layer.flatten(boolean cleanupContentStream) aceita o parâmetro booleano que especifica se deve remover os marcadores de grupo de conteúdo opcional do fluxo de conteúdo.
Definir o parâmetro cleanupContentStream como false acelera o processo de achatamento.

**Mesclar Todas as Camadas dentro do PDF em uma**

A biblioteca Aspose.PDF para Java permite mesclar todas as camadas de PDF ou uma camada específica na primeira página em uma nova camada e salva o documento atualizado.

Dois métodos foram adicionados para mesclar todas as camadas na página:

- void mergeLayers(String newLayerName);

- void mergeLayers(String newLayerName, String newOptionalContentGroupId);

O segundo parâmetro permite renomear o marcador de grupo de conteúdo opcional. O valor padrão é "oc1" (/OC /oc1 BDC).

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    page.mergeLayers("NewLayerName");

    // Ou page.mergeLayers("NewLayerName", "OC1");

    document.save(output);
```

## O que há de novo no Aspose.PDF 24.4

Este lançamento introduziu plugins Java para PDF:

- Plugin de Achatamento de Formulário

```java

    FormFlattener pdfFormPlugin = new FormFlattener();

    FormFlattenAllFieldsOptions opt = new FormFlattenAllFieldsOptions();

    opt.addInput(new FileDataSource("sample.pdf"));
    opt.addOutput(new FileDataSource("sample-flat.pdf"));

    ResultContainer result = pdfFormPlugin.process(opt);

    // Verificar resultado.
    java.util.List < IOperationResult > resultCollectionInternal = result.getResultCollection();
```

- Exportador de Formulário

```java

    Rectangle rect = new com.aspose.pdf.Rectangle(0, 220, 600, 330);

    // Uso do plugin.
    FormExporter pdfFormPlugin = new FormExporter();
    SelectField selectField = new SelectField() {
      public boolean invoke(Field field) {
        return field instanceof TextBoxField && field.getPageIndex() == 2 && rect.isInclude(field.getRect(), 0);
      }
    };
    FormExporterValuesToCsvOptions opt = new FormExporterValuesToCsvOptions(selectField, ';');

    opt.addInput(new FileDataSource(inputFileNameWithFields));
    opt.addInput(new FileDataSource(getInputPath("document-1.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-2.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-3.pdf")));
    opt.addOutput(new FileDataSource(getOutputPath("out.csv")));
    ResultContainer result = pdfFormPlugin.process(opt);

    // Verificar resultado.
    System.out.println(result.getResultCollectionInternal().size() > 0);
    System.out.println(result.getResultCollectionInternal().get_Item(0).isFile());
    System.out.println(result.getResultCollectionInternal().get_Item(0).getData().toString());
```


- Plugin de Fusão

```java

    String input1 = "sample.pdf";
    String input2 = "sample.pdf";

    String output = "TestMergeFileAndStream_ResultAsFile.pdf";

    Merger merger = new Merger();

    MergeOptions opt = new MergeOptions();
    opt.addInput(new FileDataSource(input1));
    opt.addInput(new StreamDataSource(new FileInputStream(input2)));

    opt.addOutput(new FileDataSource(output));

    ResultContainer results = merger.process(opt);

    System.out.println(results.getResultCollection().size());
    System.out.println(results.getResultCollection().get(0).isFile());
```

- Plugin de Otimização

Como reduzir o tamanho de Documentos PDF?

```java

    String input = "Test.pdf";
    String output = "Optimized.pdf";

    Optimizer optimizer = new Optimizer();

    OptimizeOptions opt = new OptimizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    optimizer.process(opt);
```

Como redimensionar Documentos PDF?

```java

    String input = "sample.pdf";
    String output = "ResizeMain.pdf";

    Optimizer organizer = new Optimizer();

    ResizeOptions opt = new ResizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    opt.setPageSize(PageSize.getA1());

    organizer.process(opt);
```


Como rotacionar Documentos PDF?

```java

    String input = "sample.pdf";
    String output = "OptimizerRotateMain.pdf";

    Optimizer optimizer = new Optimizer();

    RotateOptions opt = new RotateOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));
    opt.setRotation(Rotation.on90);

    ResultContainer results = optimizer.process(opt);
```

## O que há de novo no Aspose.PDF 24.3

A partir do 24.3, implemente uma busca por uma lista de frases em um TextFragmentAbsorber.

```java

    String[] expressions = new String[] {
      //detectar número de telefone
      "\\b\\d{3}-\\d{3}-\\d{4}\\b",
      //detectar número de cartão
      "\\b(?:\\d[ -]*?){13,16}\\b"
    };
    Document document = new Document(input);

    TextFragmentCollection newTextFragmentCollection = new TextFragmentCollection();

    Pattern[] regexes = new Pattern[6];
    for (int i = 0; i < expressions.length; i++) {
      regexes[i] = Pattern.compile(expressions[i], Pattern.CASE_INSENSITIVE);
    }
    TextFragmentAbsorber newAbsorber = new TextFragmentAbsorber(regexes, new TextSearchOptions(true));
    document.getPages().accept(newAbsorber);
    HashMap < Pattern, TextFragmentCollection > map = newAbsorber.getRegexResults();
```


Próximo recurso é adicionar a capacidade de converter tabelas para o conversor de PDF para Markdown

```java

    Document doc = new Document(dataDir + "56201.pdf");
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    doc.save(dataDir + "56201.md", saveOptions);
```

## O que há de novo no Aspose.PDF 24.2

A partir da versão 24.2 é possível adicionar a Marca d'Água em PDF com AcroForms. TextStamp é adequado para uso com arquivos AcroForm. Se você usar TextStamp para arquivos XFA, o texto é desenhado na página como em um arquivo PDF usual (pode ser visto naqueles visualizadores de PDF que não conseguem ler arquivos XFA, por exemplo, no navegador Chrome). Para adicionar texto ao arquivo XFA, ele deve ser alterado no XML interno do arquivo XFA.

```java

    String sourceName = dataDir + "551.3xfa.pdf";
    String targetName = dataDir + "output_2_" + BuildVersionInfo.AssemblyVersion + ".pdf";

    Document pdfDocument = new Document(sourceName);
    XFA xfa = pdfDocument.getForm().getXFA();

    String watermark =
    "<subform>" +
    "<draw rotate=\"90\" x=\"100px\" y=\"100px\">" +
    "<value>" +
    "<text>Sample Stamp</text>\n" +
    "</value>" +
    "<font typeface=\"Arial\" size=\"14px\" weight=\"bold\" posture=\"italic\">" +
    "<fill>" +
    "<color value=\"0,128,0\"/>" +
    "</fill>" +
    "</font>" +
    "</draw>" +
    "</subform>";

    xfa.appendToTemplate("//tpl:pageArea", watermark);

    pdfDocument.save(targetName);
    pdfDocument.close();
```


Set StateModel para Anotação
Podemos usar setReviewState e setMarkedState da classe MarkupAnnotation para definir o estado necessário.
Todas as anotações de marcação têm uma opção Definir Estado disponível.

```java

    // Abra o documento PDF de origem
    Document pdfDocument = new Document();
    pdfDocument.getPages().add();
    // Criar anotação
    TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.getPages().get_Item(1), new Rectangle(200,
            400, 400, 600));

    // Definir título da anotação
    textAnnotation.setTitle("Título de Anotação de Exemplo");

    // Definir assunto da anotação
    textAnnotation.setSubject("Assunto de Exemplo");
    // Especificar o conteúdo da anotação
    textAnnotation.setContents("Conteúdo de exemplo para a anotação");
    textAnnotation.setOpen(true);
    textAnnotation.setIcon(TextIcon.Key);
    com.aspose.pdf.Border border = new com.aspose.pdf.Border(textAnnotation);
    border.setWidth(5);
    border.setDash(new Dash(1, 1));
    textAnnotation.setBorder(border);
    String userName1 = "Aspose1";
    textAnnotation.setReviewState(AnnotationState.Rejected, userName1);
    textAnnotation.setRect(new Rectangle(200, 400, 400, 600));

    // Adicionar anotação na coleção de anotações da página
    pdfDocument.getPages().get_Item(1).getAnnotations().add(textAnnotation);
    pdfDocument.processParagraphs();

    // Salvar o arquivo de saída
    pdfDocument.save(dataDir + "output_24_2_Rejected.pdf");

    pdfDocument = new Document(dataDir + "output" + version + "3.pdf");
    TextAnnotation textAnnotation2 = (TextAnnotation) pdfDocument.getPages().get_Item(1).getAnnotations().get_Item(1);

    String userName2 = "Aspose2";
    textAnnotation2.setReviewState(AnnotationState.Accepted, userName2);
    pdfDocument.save(dataDir + "output_24_2_Rejected_and_Accepted.pdf");
```


A partir da versão 24.2 implementar a conversão de OFD para PDF:

```java

    Document document = new Document(inputPath, new OfdLoadOptions());
    document.save(outputPath);
```

## O que há de novo no Aspose.PDF 24.1

A partir da versão 24.1 implementar a conversão de PDF para Markdown:

```java

    final Document doc = new Document(inputPdfPath);
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Outlines);
    doc.save(markdownOutputFilePath, saveOptions);
```

Além disso, na versão 24.1 a interrupção de thread usando o InterruptMonitor foi implementada.

```java

    final InterruptMonitor monitor = new InterruptMonitor();

    new Thread(new Runnable() {

      public void run() {

        InterruptMonitor.setThreadLocalInstance(monitor);
        Document document = new Document();

        try {
          Page page = document.getPages().insert(1);
          PageInfo pageInfo = page.getPageInfo();
          pageInfo.setLandscape(true);
          Table topicTable = new Table();
          topicTable.setBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setColumnWidths("5% 10% 5% 60% 10% 10%");
          topicTable.setRepeatingRowsCount(1);

          Row topicRow = topicTable.getRows().add();

          topicRow.getCells().add("texto");
          topicRow.getCells().add("texto");
          topicRow.getCells().add("texto");
          topicRow.getCells().add("texto");
          topicRow.getCells().add("texto");
          topicRow.getCells().add("texto");

          //conversão de declarações foreach para while
          Iterator tmp0 = (topicRow.getCells()).iterator();
          while (tmp0.hasNext()) {
            Cell cell = (Cell) tmp0.next();
            cell.setVerticalAlignment(VerticalAlignment.Center);
            cell.setAlignment(HorizontalAlignment.Center);
          }

          Row row2 = topicTable.getRows().add();
          row2.getCells().add("texto");
          row2.getCells().add("texto");
          row2.getCells().add("texto");
          String LongText = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.";
          row2.getCells().add(LongText);
          row2.getCells().add("texto");
          row2.getCells().add("texto");
          page.getParagraphs().add(topicTable);
          document.save(dataDir + "out" + version + ".pdf");

        } catch (com.aspose.pdf.exceptions.OperationCanceledException ex) {
          System.out.println("Interrompendo a thread de salvamento em " + System.currentTimeMillis());
        } finally {
          if (document != null) {
            document.close();
          }
        }

      }

    }).start();

    System.out.println("Processo iniciado em thread em " + System.currentTimeMillis());

    // O tempo limite deve ser menor que o tempo necessário para salvar o documento completo (sem interrupção).
    Thread.sleep(500);

    // Interromper o processo
    monitor.interrupt();

    System.out.println("Interrompeu a thread de salvamento em " + System.currentTimeMillis());
```


## O que há de novo no Aspose.PDF 23.12

O formulário pode ser encontrado e o texto pode ser substituído usando o seguinte trecho de código:

```java

    Document document = new Document(input);
    String expectedText = "Este é um texto adicionado ao criar um novo PDF no Kofx Power PDF Standard.";

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
      XForm form = (XForm) tmp0.next();
      if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(form);

        Iterator tmp1 = (absorber.getTextFragments()).iterator();
        while (tmp1.hasNext()) {
          TextFragment fragment = (TextFragment) tmp1.next();
          fragment.setText("");
        }
      }
    }

    document.save(output);
```            

Ou, o formulário pode ser completamente removido:

```java

    Document document = new Document(input);
    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    // Conversão de declarações foreach para while
    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
        XForm form = (XForm) tmp0.next();
        if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
            String name = forms.getFormName(form);
            forms.delete(name);
        }
    }

    document.save(output);
```            


Outra variante de remoção do formulário:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    for (int i = 1; i <= forms.size(); i++) {
        if ("Typewriter".equals(forms.get_Item(i).getIT()) && "Form".equals(forms.get_Item(i).getSubtype())) {
            forms.delete(forms.get_Item(i).getName());
        }
    }

    document.save(output);
``` 

- Todos os formulários podem ser excluídos usando o seguinte trecho de código:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    forms.clear();

    document.save(output);
```

## O que há de novo no Aspose.PDF 23.11

A partir deste lançamento é possível remover texto oculto do arquivo PDF:

```java

    Document document = new Document(inputFile);

    TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
    textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
    document.getPages().accept(textAbsorber);

    msStringBuilder result = new msStringBuilder();

    // Conversão de declarações foreach para while
    Iterator tmp0 = (textAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext()) {
            TextFragment fragment = (TextFragment) tmp0.next();
            if (fragment.getTextState().isInvisible()) {
                result.append(fragment.getText());
                fragment.setText("");
            }
        }

    document.save(outputFile);
```


## O que há de novo no Aspose.PDF 23.10

A atualização atual apresenta três versões de Remoção de tags de PDFs marcados.

- Remover algum elemento de nó de um documentElement (elemento raiz da árvore):

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element documentElement = structure.getChildren().get_Item(0);
    Element structElement = (documentElement.getChildren().getCount() > 1) ?  documentElement.getChildren().get_Item(1) : null;
    documentElement.getChildren().remove(structElement);
    // Você também pode excluir o próprio structElement
                //if (structElement != null)
                //{
                //    structElement.remove();
                //}
    document.save(outputPath);
```

- Remover todas as tags de elementos marcados do documento, mas manter os elementos da estrutura:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root= structure.getChildren().get_Item(0);
    Queue<Element> queue = new ArrayDeque<Element>();
    queue.add(root);
    for (Element element : structure.getChildren() ) {
        queue.add(element);
        for (Element child : element.getChildren())
        {
            queue.add(child);
        }
    }
    for (Element element:queue ) {
        if (element instanceof TextElement  || element instanceof FigureElement)
            element.remove();
    }
    document.save(outputPath);
```


- Remover todas as tags:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root = structure.getChildren().get_Item(0);
    root.remove();
    document.save(outputPath);
```

Implementamos um novo recurso para medir a altura de um caractere. Use o seguinte código para medir a altura de um caractere:

```java

    Document doc = new Document("input.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.visit(doc.getPages().get_Item(1));
    double height = absorber.getTextFragments().get_Item(1).getTextState().measureHeight('h')
```

Note que a medição é baseada na fonte incorporada no documento. Se alguma informação para uma dimensão estiver faltando, este método retorna 0.

## O que há de novo no Aspose.PDF 23.9

A partir do 23.9, suporte para remover uma anotação filha de um campo preenchível.

exemplo 1:

```java

    String input = "55343_1.pdf";
    Document doc = new Document(input);
    final String fieldName = "1 Vehicle Identification Number";
    Field field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
    Rectangle rect = field.getRect();
    doc.getForm().addFieldAppearance(field, 2, rect);
    System.out.println(2 == field.size());

    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(2 == field.size());
    doc.getForm().removeFieldAppearance(field, 1);

    System.out.println(0 == field.size());
    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
```


example 2:

```java

    {
    String option1 = "opção 1";
    String option2 = "opção 2";
    String outputPdf = "saída.pdf";

    final Document document = new Document();
    try /*JAVA: estava usando*/ {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

        // Defina o valor da primeira opção do grupo de caixas de seleção
        checkbox.setExportValue(option1);
        checkbox.addOption(option2);
        document.getForm().add(checkbox);
        java.util.List < String > tmp0 = new ArrayList < String > ();
        tmp0.add("Off");
        tmp0.add(option1);
        tmp0.add(option2);
        System.out.println(collectionAssert_AreEqual(tmp0, checkbox.getAllowedStates()));
        checkbox.setValue(option2);

        WidgetAnnotation f = document.getForm().get_Item(1);
        document.getForm().removeFieldAppearance((Field) f, 2);

        checkbox = (CheckboxField) document.getForm().get_Item(1);
        java.util.List < String > tmp1 = new java.util.ArrayList < String > ();
        tmp1.add("Off");
        tmp1.add(option1);
        System.out.println(collectionAssert_AreEqual(tmp1, checkbox.getAllowedStates()));

        document.save(outputPdf);
    } finally {
        if (document != null)(document).close();
    }
    }
    public static boolean collectionAssert_AreEqual(java.util.List < String > value1,
    java.util.List < String > value2) {
    if (value1.size() == value2.size()) {
        for (int i = 0; i < value1.size(); i++) {
        if (!value1.get(i).equals(value2.get(i)))
            return false;
        }
    } else {
        return false;
    }
    return true;
    }
```


Adicionando imagem com ImageFilterType.Flate não preserva a transparência.

```java

    Document document = new Document();
    Page page = document.getPages().add();

    FileInputStream stream = new FileInputStream(("55037_1.png"));

    page.getResources().getImages().addWithImageFilterType(stream, ImageFilterType.Flate);
    page.getContents().add(new GSave());
    Rectangle rectangle = new Rectangle(413, 428, 548, 564);
    Matrix matrix = new Matrix(
      new double[] {
        rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY()
      });

    page.getContents().add(new ConcatenateMatrix(matrix));
    XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
    page.getContents().add(new Do(ximage.getName()));
    page.getContents().add(new GRestore());
    document.save(getOutputPath("55157.pdf"));
    stream.close();
```

## O que há de novo no Aspose.PDF 23.8

A função para detectar Atualizações Incrementais em um documento PDF foi adicionada na versão 23.8. Esta função retorna 'true' quando o documento foi salvo com atualizações incrementais, caso contrário, retorna 'false'.

```java

    Document doc = new Document(dataDir+"PDF_Support_Tech_Note.pdf");
    boolean not_updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(not_updatedIncrementally);

    doc.getPages().add();
    doc.saveIncrementally(dataDir+"PDF_updatedIncrementally.pdf");

    doc = new Document(dataDir+"PDF_updatedIncrementally.pdf");
    boolean updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(updatedIncrementally);
    doc.close();
```    

Mais uma funcionalidade é Copiar OutputIntents do PDF de entrada para o PDF de destino.

Adicionamos uma nova propriedade pública Document.getOutputIntents() para permitir o acesso aos intents de saída em um documento. Por enquanto, apenas o uso dos intents de saída já existentes em algum documento é suportado, o usuário não pode criar OutputIntent do zero.

```java

    Document document1 = new Document(dataDir+"pdfa.pdf");
    Document resultDocument = new Document();
    resultDocument.getPages().add(document1.getPages());

    for (OutputIntent intent : document1.getOutputIntents())
    {
        resultDocument.getOutputIntents().addItem(intent);
    }

    resultDocument.save(dataDir+"resultpath.pdf");
```  


From Aspose.PDF 23.8 suporte para adicionar a extração de formas:

```java

{
    String input1 = getInputPdf("46298_1");
    String input2 = getInputPdf("46298_2");

    Document source = new Document(input1);
    Document dest = new Document(input2);

    Page destPage = dest.getPages().get_Item(1);

    TextFragmentAbsorber tfAbsorber = new TextFragmentAbsorber();
    tfAbsorber.visit(source.getPages().get_Item(1));

    // conversão de declarações foreach para while
    Iterator tmp0 = ( tfAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext())
        {
            TextFragment textFragment = (TextFragment)tmp0.next();
            System.out.println(textFragment.getText());
            addTextImproved(destPage, textFragment);
        }

    ImagePlacementAbsorber imageAbsorber = new ImagePlacementAbsorber();
    imageAbsorber.visit(source);

    Iterator tmp1 = ( imageAbsorber.getImagePlacements()).iterator();
        while (tmp1.hasNext())
        {
            ImagePlacement image = (ImagePlacement)tmp1.next();
            destPage.addImage(image.getImage().toStream(), image.getRectangle());
        }

    GraphicsAbsorber vectorAbsorber = new GraphicsAbsorber();
    vectorAbsorber.visit(source.getPages().get_Item(1));
    Rectangle area = new Rectangle(90, 250, 300, 400);
    dest.getPages().get_Item(1).addGraphics(vectorAbsorber.getElements(), area);
    dest.save(getOutputPath("46298-out.pdf"));
    }

    private static void addTextImproved(Page page, TextFragment textFragment)
    {
        TextFragment local = new TextFragment();
        local.setPosition(textFragment.getPosition());

        // Recalcular uma nova posição, pois o tamanho da página difere do PDF original
        local.getPosition().setXIndent(textFragment.getPosition().getXIndent());//2.5 * 72;
        double newPageHeight = page.getPageRect(true).getHeight();
        double oldPageHeight = textFragment.getPage().getPageRect(true).getHeight();
        local.getPosition().setYIndent(textFragment.getPosition().getYIndent());

        local.setText(textFragment.getText());
        local.getTextState().setFont(textFragment.getTextState().getFont());
        local.getTextState().setFontSize(textFragment.getTextState().getFontSize());

        local.getTextState().setFormattingOptions(textFragment.getTextState().getFormattingOptions());
        local.getTextState().setForegroundColor(textFragment.getTextState().getForegroundColor());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(local);
    }
```


Também suporta a capacidade de detectar Overflow ao adicionar texto:

```java

    Document doc = new Document();
    String paragraphContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan.";
    Rectangle rectangle = new Rectangle(100, 600, 500, 700, false);
    TextParagraph paragraph = new TextParagraph();
    TextFragment fragment = new TextFragment(paragraphContent);
    paragraph.setVerticalAlignment(VerticalAlignment.Top);
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    paragraph.setRectangle(rectangle);
    boolean isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    while (!isFitRectangle)
    {
        fragment.getTextState().setFontSize(fragment.getTextState().getFontSize() - 0.5f);
        isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    }
    paragraph.appendLine(fragment);
    TextBuilder builder = new TextBuilder(doc.getPages().add());
    builder.appendParagraph(paragraph);
    doc.save(output);
```


## O que há de novo no Aspose.PDF 23.7

A partir da versão 23.7, suporte para as configurações de escala da página no diálogo de impressão:

```java

    Document document = new Document();
    document.getPages().add();
    document.setPrintScaling(PrintScaling.None);//PrintScaling.Default
    document.save(outputPdf);

    Document documentOutput = new Document(outputPdf);
    int printScaling = documentOutput.getPrintScaling();
    System.out.println("PrintScaling: " + printScaling);
```

## O que há de novo no Aspose.PDF 23.6

A partir da versão 23.6, suporte para adicionar a capacidade de definir o título da página HTML, Epub.

código para HTML:

```java

    HtmlSaveOptions options = new HtmlSaveOptions();
    options.setFixedLayout(true);
    options.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
    options.setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml);
    options.setTitle("</title>NOVA PÁGINA & TÍTULO</head>");

    Document document = new Document(inputPath);
    document.save(outPath, options);
```


código para EPUB:

```java

    EpubSaveOptions epubSaveOptions = new EpubSaveOptions();
    epubSaveOptions.setTitle("</title>NOVA PÁGINA & TÍTULO</head>");
    epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

    Document document = new Document(inputPath);
    document.save(outPath, epubSaveOptions);
```

A partir de 23.6 suporte para fornecer uma API para posicionamento de gráficos vetoriais:

```java

    Document document = new Document(input);
    VectorGraphicsAbsorber vectorAbsorber = new VectorGraphicsAbsorber();
    vectorAbsorber.visit(document.getPages().get_Item(1));

    SubPath subPath1 = vectorAbsorber.getSubPaths().get_Item(2);
    SubPath subPath2 = vectorAbsorber.getSubPaths().get_Item(3);
    SubPath subPath3 = vectorAbsorber.getSubPaths().get_Item(4);

    Point point1 = new Point(subPath1.getPosition().getX() + 200, subPath1.getPosition().getY() - 100);
    Point point2 = new Point(subPath2.getPosition().getX() + 200, subPath2.getPosition().getY() - 100);
    Point point3 = new Point(subPath3.getPosition().getX() + 200, subPath3.getPosition().getY() - 100);

    subPath1.setPosition(point1);
    subPath2.setPosition(point2);
    subPath3.setPosition(point3);

    document.save(output);
```

## O que há de novo no Aspose.PDF 23.1

A partir da versão 23.1, suporte para criar anotação PrinterMark. Adicionada uma das variantes de anotação: ColorBarAnnotation.

```java

    Document doc = new Document();
    Page page = doc.getPages().add();
    page.setTrimBox(new com.aspose.pdf.Rectangle(20, 20, 580, 820));
    Rectangle rectBlack = new com.aspose.pdf.Rectangle(100, 300, 300, 320);
    Rectangle rectCyan = new com.aspose.pdf.Rectangle(200, 600, 260, 690);
    Rectangle rectMagenta = new com.aspose.pdf.Rectangle(10, 650, 140, 670);

    ColorBarAnnotation colorBarBlack = new ColorBarAnnotation(page, rectBlack);
    ColorBarAnnotation colorBarCyan = new ColorBarAnnotation(page, rectCyan, ColorsOfCMYK.Cyan);
    ColorBarAnnotation colorBaMagenta = new ColorBarAnnotation(page, rectMagenta);
    colorBaMagenta.setColorOfCMYK(ColorsOfCMYK.Magenta);
    ColorBarAnnotation colorBarYellow = new ColorBarAnnotation(page, new com.aspose.pdf.Rectangle(400, 250, 450, 700), ColorsOfCMYK.Yellow);

    page.getAnnotations().add(colorBarBlack);
    page.getAnnotations().add(colorBarCyan);
    page.getAnnotations().add(colorBaMagenta);
    page.getAnnotations().add(colorBarYellow);
    doc.save("outFile.pdf");
```


## O que há de novo no Aspose.PDF 22.12

A partir desta versão, há suporte para converter PDF para imagem DICOM:

```java

    DicomDevice device = new DicomDevice(PageSize.getA4());
    Document doc = new Document("Input.pdf");
    ByteArrayOutputStream stream = new ByteArrayOutputStream();
    device.process(doc.getPages().get_Item(1), stream);
```

## O que há de novo no Aspose.PDF 22.9

A partir da versão 22.09, suporte para adicionar a propriedade para modificar a ordem das rubricas do assunto (E=, CN=, O=, OU=,) na assinatura.

```java

    String inputPdf = getInputPath("input.pdf");
    String inputPfx = getInputPath("input.pfx");
    String outputPdf = getOutputPath("out.pdf");

    final PdfFileSignature fileSign = new PdfFileSignature();
    try 
    {
        fileSign.bindPdf(inputPdf);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 400, 100);
        PKCS7Detached signature = new PKCS7Detached(inputPfx, "123456789");
        signature.setDate(new Date());
        signature.setCustomAppearance( new SignatureCustomAppearance());
        signature.getCustomAppearance().setUseDigitalSubjectFormat(true);
        signature.getCustomAppearance().setDigitalSubjectFormat(new /*SubjectNameElements*/int[] { SubjectNameElements.CN, SubjectNameElements.O });

        fileSign.sign(1, true, rect, signature);
        fileSign.save(outputPdf);
    }
    finally { 
        if (fileSign != null) 
            fileSign.close(); 
    }
```

## O que há de novo no Aspose.PDF 22.8

A partir do Aspose.PDF 23.8 suporte para adicionar método para reconstruir tabela xref:

```java

    PdfFileSanitization sanitizer = new PdfFileSanitization();
    try {
        sanitizer.bindPdf(dataDir + "50528_1.pdf");
        sanitizer.rebuildXrefAndTrailer();
        sanitizer.save(dataDir + "50528_1" + version + ".pdf");
    } finally {
        if (sanitizer != null) ( sanitizer).close();
    }
```

## O que há de novo no Aspose.PDF 22.6

PDF para PDF_A_1A - implementar opção para remover cor de transparência para evitar tamanho grande do arquivo de saída.

A partir da versão 22.5 o cliente pode controlar a qualidade da transparência convertida, e o tamanho do arquivo de saída como resultado:

```java
    opts.setTransparencyResolution(300);
```

## O que há de novo no Aspose.PDF 22.5

Durante a conversão para PDF/A o conteúdo transparente é removido e substituído por imagem. Implementamos um novo recurso, e agora o cliente pode controlar a qualidade da imagem com o parâmetro TransparencyResolution:

```java

    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
    PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
    options.setTransparencyResolution(300);
    pdfDocument.convert(options);
    pdfDocument.save("finalOutput.pdf");
```


## O que há de novo no Aspose.PDF 22.4

Este lançamento inclui informações para Aspose.PDF para Java:

- PDF para ODS: Reconhecer texto em subscrito e sobrescrito;

**exemplo**

```java

    Document pdfDocument = new Document("Superscript-Subscript.pdf");
    ExcelSaveOptions options = new ExcelSaveOptions();
    options.Format = ExcelSaveOptions.ExcelFormat.ODS;
    pdfDocument.Save("output.ods"), options);
```

- PDF para XMLSpreadSheet2003: Reconhecer texto em subscrito e sobrescrito;

- PDF para Excel: Reconhecer texto em subscrito e sobrescrito;

## O que há de novo no Aspose.PDF 22.3

PDF para ODS: Suporte para RTL está disponível na versão 22.3

```java

    ExcelSaveOptions options = new ExcelSaveOptions();
    options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
    pdfDocument.save("output.ods", options);
```

## O que há de novo no Aspose.PDF 22.2

Este lançamento inclui o PDF para XSLX: Suporte para RTL (Hebraico, Árabe).

## O que há de novo no Aspose.PDF 22.1

Aspose.PDF para Java permite carregar documentos Portable Document Format (PDF) versão 2.0.

## O que há de novo no Aspose.PDF 21.10

### Como detectar texto oculto?

Por favor, use o seguinte código:

```java

Document pdf = new Document(inFile);
        Page page = pdf.getPages().get_Item(1);
        TextFragmentAbsorber textFragmentAbsorber = new com.aspose.pdf.TextFragmentAbsorber();
        page.accept(textFragmentAbsorber);
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

        int fragmentsCount = textFragmentAbsorber.getTextFragments().size();
        int invisibleCount = 0;

        Iterator tmp0 = ( textFragmentCollection).iterator();
            while (tmp0.hasNext())
            {
                com.aspose.pdf.TextFragment fragment = (com.aspose.pdf.TextFragment)tmp0.next();
                System.out.println(fragment.getText());
                System.out.println(fragment.getTextState().isInvisible());
                if (fragment.getTextState().isInvisible())
                    invisibleCount++;
            }
```


## O que há de novo no Aspose.PDF 21.8

### Como alterar a cor do texto na Assinatura Digital?

Na versão 21.8, setForegroundColor permite alterar a cor do texto na Assinatura Digital:

```java
Por favor, use o seguinte código:

                    PdfFileSignature pdfSign = new PdfFileSignature();                
                    pdfSign.bindPdf(inFile);
                    //criar um retângulo para a localização da assinatura
                    java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);
                    PKCS7 pkcs = new PKCS7(inPfxFile, "");

                    pkcs.setCustomAppearance( new SignatureCustomAppearance());
//definir cor do texto
                    pkcs.getCustomAppearance().setForegroundColor(Color.getGreen());

                    // assinar o arquivo PDF
                    pdfSign.sign(1, true, rect, pkcs);
                    //salvar arquivo PDF de saída
                    pdfSign.save(outFile);
```

## O que há de novo no Aspose.PDF 21.6

### Ocultando imagem usando ImagePlacementAbsorber do documento

Com Aspose.PDF para Java, você pode ocultar imagens usando ImagePlacementAbsorber do documento:

```java
      Document doc = new Document("input.pdf");

        for (Page page : doc.getPages()) {
            ImagePlacementAbsorber ipa = new ImagePlacementAbsorber();
            ipa.visit(page);
            for (ImagePlacement ip : ipa.getImagePlacements()) {
                ip.hide();
            }
        }

        doc.save("out.pdf");
```

## O que há de novo no Aspose.PDF 21.5

### Adicionar API para mesclar imagens

Aspose.PDF 21.4 permite combinar imagens. Mescla lista de fluxos de imagem como um fluxo de imagem único. Formatos de saída Png/jpg/tiff são suportados, no caso de uso de formato não suportado, o fluxo de saída é codificado como Jpeg por padrão.
Siga o próximo trecho de código:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile300dpi = new FileInputStream("image1.jpg");
        try  {
            inputImagesStreams.add(inputFile300dpi);
            InputStream inputFile600dpi = new FileInputStream("image2.jpg");
            try {
                inputImagesStreams.add(inputFile600dpi);
                inputStream = PdfConverter.mergeImages(
                        inputImagesStreams,
                        com.aspose.pdf.ImageFormat.Jpeg,
                        ImageMergeMode.Vertical,
                        new Integer(1),
                        new Integer(1)
                );
            } finally {
                if (inputFile600dpi != null) (inputFile600dpi).close();
            }
        } finally {
            if (inputFile300dpi != null) (inputFile300dpi).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out.pdf");
        inputStream.close();
```


Você também pode mesclar suas imagens no formato Tiff:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile1 = new FileInputStream("1.tif");
        try  {
            inputImagesStreams.add(inputFile1);
            InputStream inputFile2 = new FileInputStream("2.tif");
            try {
                inputImagesStreams.add(inputFile2);
                inputStream = PdfConverter.mergeImagesAsTiff(inputImagesStreams);
            } finally {
                if (inputFile2 != null) (inputFile2).close();
            }
        } finally {
            if (inputFile1 != null) (inputFile1).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out2.pdf");
        inputStream.close();
```

## O que há de novo no Aspose.PDF 21.02

Aspose.PDF v21.02 Assinar PDF com Assinaturas PAdES LTV

```java
final Document document = new Document(inputPdf);
    try 
    {
        PdfFileSignature signature = new PdfFileSignature(document);
        PKCS7 pkcs7 = new PKCS7(getInputPath("cert.pfx"), "password");
        //Assinar PDF com Assinaturas PAdES LTV
        pkcs7.setUseLtv(true);

        signature.sign(1, true, new Rectangle(100, 100, 300, 300), pkcs7);
        signature.save(outputPdf);
    }
    finally { if (document != null) (document).dispose(); }
```