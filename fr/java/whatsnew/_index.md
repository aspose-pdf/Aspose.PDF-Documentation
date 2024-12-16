---
title: Quoi de neuf 
linktitle: Quoi de neuf
type: docs
weight: 10
url: /fr/java/whatsnew/
description: Cette page présente les fonctionnalités nouvelles les plus populaires dans Aspose.PDF pour Java qui ont été introduites dans les versions récentes.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-06-05"
---

## Quoi de neuf dans Aspose.PDF 24.8

Depuis 24.8, prise en charge du format PDF/A-4 :

```java

    Document document = new Document(inputPdf);
    // Seuls les documents PDF-2.x peuvent être convertis en PDF/A-4
    document.convert(new ByteArrayOutputStream(), PdfFormat.v_2_0, ConvertErrorAction.Delete);
    boolean converted = document.convert(logFile, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
    document.save(outputFile);
```

Il est également possible d'ajouter un texte alternatif pour le tampon d'image :

La propriété AlternativeText a été ajoutée à ImageStamp - si une valeur lui est attribuée, alors lors de l'ajout d'un ImageStamp à un document, il a un texte alternatif.

```java

    String p1_Alt1 = "*** page 1, texte alternatif 1 ***",
                    p1_Alt2 = "*** page 1, texte alternatif 2 ***",
                    p2_Alt1 = "--- page 1, texte alternatif 1 ---",
                    p2_Alt2 = "--- page 1, texte alternatif 2 ---";

    StructTreeRootElement structTreeRoot = document.getTaggedContent().getStructTreeRootElement();

    ImageStamp imageStamp = new ImageStamp(dataDir + "test.jpg");
    imageStamp.setXIndent(100);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setQuality(100);
    imageStamp.setAlternativeText(p1_Alt1);

    // À la page 1
    document.getPages().get_Item(1).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p1_Alt2);
    document.getPages().get_Item(1).addStamp(imageStamp);

    // À la page 2
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

    // Enregistrer le document
    document.save(outFile);
```


Aussi, le code suivant montre comment ajouter un texte alternatif dans les images existantes dans FigureElements.

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

            // Définir le texte alternatif
            figureElement.setAlternativeText("Texte alternatif de figure (technique 1)");
        }
    }

    // Enregistrer le document
    document.save(outFile);
```


## Quoi de neuf dans Aspose.PDF 24.7

Depuis la version 24.7, dans le cadre de l'édition de PDF balisé, des méthodes ont été ajoutées sur **Aspose.Pdf.LogicalStructure.Element** :

- Tag (ajouter des balises à des opérateurs spécifiques comme des images, du texte et des liens)
- InsertChild
- RemoveChild
- ClearChilds

Ces méthodes vous permettent de modifier les balises des fichiers PDF, par exemple :

```java

    Document document = new Document(dataDir + "test.pdf");

    // Récupérer la première page du document.
    Page page = document.getPages().get_Item(1);

    // Initialiser des variables pour contenir les éléments BDC (Begin Dictionary Context) à différentes fins.
    BDC imageBdc = null;
    BDC pBdc = null;
    BDC link1Bdc = null;
    BDC link2Bdc = null;
    BDC helloBdc = null;

    // Itérer sur le contenu de la page.
    for (int i = 1; i <= page.getContents().size(); i++)
    {
        // Obtenir l'opérateur courant du contenu de la page.
        Operator op = page.getContents().get_Item(i);

        // Vérifier si l'opérateur est une instance de BDC.
        if (op instanceof BDC) {
        BDC bdc = (BDC)op; // Convertir l'opérateur en type BDC.
        if (bdc != null)
        {
            // Vérifier si le MCID (Mark Content Identifier) du BDC est 0.
            if (bdc.getProperties().getMCID()[0] != null && bdc.getProperties().getMCID()[0] == 0)
            {
                helloBdc = bdc; // Stocker le BDC pour une utilisation ultérieure.
            }
        }
    }

    // Vérifier si l'opérateur est une instance de Do (Draw Object).
    if (op instanceof Do) {
        Do doXobj = (Do)op; // Convertir l'opérateur en type Do.
        if (doXobj != null)
        {
            // Créer un nouveau BDC pour une image et l'insérer dans le contenu de la page.
            imageBdc = new BDC("Figure");
            page.getContents().insert(i - 2, imageBdc); // Insérer avant l'opérateur courant.
            i++; // Incrémenter l'index pour prendre en compte le BDC inséré.
            page.getContents().insert(i + 1, new EMC()); // Insérer un EMC (End Mark Content).
            i++; // Incrémenter à nouveau l'index.
        }
    }

    // Vérifier si l'opérateur est une instance de TextShowOperator (pour l'affichage de texte).
    if (op instanceof TextShowOperator) {
        TextShowOperator tx = (TextShowOperator)op; // Convertir l'opérateur en type TextShowOperator.
        if (tx != null)
        {
            // Vérifier le contenu textuel spécifique et insérer les BDC correspondants.
            if (tx.getText().contains("efter Ukendt forfatter er licenseret under"))
            {
                pBdc = new BDC("P");
                page.getContents().insert(i - 1, pBdc); // Insérer avant l'opérateur courant.
                i++; // Incrémenter l'index.
                page.getContents().insert(i + 1, new EMC()); // Insérer un EMC.
                i++; // Incrémenter l'index.
            }
            if (tx.getText().contains("CC"))
            {
                link1Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link1Bdc); // Insérer avant l'opérateur courant.
                i++; // Incrémenter l'index.
                page.getContents().insert(i + 1, new EMC()); // Insérer un EMC.
                i++; // Incrémenter l'index.
            }
            if (tx.getText().contains("Dette billede"))
            {
                link2Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link2Bdc); // Insérer avant l'opérateur courant.
                i++; // Incrémenter l'index.
                page.getContents().insert(i + 1, new EMC()); // Insérer un EMC.
                i++; // Incrémenter l'index.
            }
        }
    }
}
 
    // Récupérer le contenu balisé du document.
    ITaggedContent tagged = document.getTaggedContent();

    // Traiter le contenu balisé pour modifier les attributs de structure.
    // Obtenir le premier élément enfant de l'élément racine dans le contenu balisé.
    com.aspose.pdf.tagged.logicalstructure.elements.Element p = tagged.getRootElement().getChildElements().get_Item(1);
    p.clearChilds(); // Effacer les éléments enfants existants.

    // Baliser le helloBdc avec l'élément de structure parent.
    MCRElement mcr = p.tag(helloBdc);

    // Créer et définir des attributs de structure pour l'élément balisé.
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
            .getAttributes().createAttributes(AttributeOwnerStandard.Layout);
    StructureAttribute attr = new StructureAttribute(AttributeKey.SpaceAfter);
    attr.setNumberValue(30.625); // Définir l'attribut d'espace après.
    attrs.setAttribute(attr); // Appliquer l'attribut à la structure.

    // Créer un nouvel FigureElement dans le contenu balisé.
    com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figure = tagged.createFigureElement();
    tagged.getRootElement().insertChild(figure, 2); // Insérer l'élément figure à la deuxième position.
    figure.setAlternativeText("Une mouche."); // Définir le texte alternatif pour la figure.

    // Baliser l'imageBdc avec l'élément figure.
    MCRElement mcr = figure.tag(imageBdc);

    // Récupérer l'élément de structure parent du MCR (Marked Content Reference) spécifié
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Créer un nouvel attribut de structure pour l'espace après l'élément
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(3.625); // Définir la valeur de l'espace après à 3,625 unités
    attrs.setAttribute(spaceAfter); // Assigner l'attribut d'espace après aux attributs de structure

    // Créer un nouvel attribut de structure pour le cadre de délimitation (BBox)
    StructureAttribute bbox = new StructureAttribute(AttributeKey.BBox);
    bbox.setArrayNumberValue(new Double[][] { new Double[] { (71.9971) }, new Double[] { (375.839) }, new Double[] { (523.299) }, new Double[] { (714.345) } });
    // Définir les valeurs du cadre de délimitation pour l'attribut de structure
    attrs.setAttribute(bbox); // Assigner l'attribut de cadre de délimitation aux attributs de structure

    // Créer un nouvel attribut de structure pour le placement
    StructureAttribute placement = new StructureAttribute(AttributeKey.Placement);
    placement.setNameValue(AttributeName.Placement_Block); // Définir le type de placement à bloc
    attrs.setAttribute(placement); // Assigner l'attribut de placement aux attributs de structure

    // Récupérer le quatrième élément enfant de l'élément racine de la structure balisée
    StructureElement p2 = (StructureElement)tagged.getRootElement().getChildElements().get_Item(3);
    p2.clearChilds(); // Effacer les éléments enfants existants de p2

    // Créer un nouvel élément SpanElement à ajouter à p2
    SpanElement span1 = tagged.createSpanElement();

    // Créer des attributs de structure pour l'élément span
    StructureAttributes attrs = span1.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Créer un nouvel attribut de structure pour le type de décoration du texte
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Définir la décoration du texte en soulignement
    attrs.setAttribute(textDecorationType); // Assigner l'attribut de type de décoration du texte aux attributs de structure

    // Créer un nouvel attribut de structure pour l'épaisseur de la décoration du texte
    StructureAttribute textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
    textDecorationThickness.setNumberValue(0); // Définir l'épaisseur de la décoration du texte à 0
    attrs.setAttribute(textDecorationThickness); // Assigner l'attribut d'épaisseur de décoration du texte aux attributs de structure

    // Créer un nouvel attribut de structure pour la couleur de la décoration du texte
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
    textDecorationColor.setArrayNumberValue(new Double[][] { new Double[] { (0.0196075) }, new Double[] { (0.384308) }, new Double[] { (0.756866) } });
    // Définir les valeurs RGB pour la décoration du texte
    attrs.setAttribute(textDecorationColor); // Assigner l'attribut de couleur de décoration du texte aux attributs de structure

    p2.appendChild(span1); // Ajouter l'élément span1 à p2


    // Créer un nouvel élément MCR et le baliser avec pBdc
    MCRElement mcr = p2.tag(pBdc);
    // Récupérer l'élément de structure parent du MCR et créer des attributs de mise en page
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Créer un nouvel attribut de structure pour l'alignement du texte
    StructureAttribute textAlign = new StructureAttribute(AttributeKey.TextAlign);
    textAlign.setNameValue(AttributeName.TextAlign_Center); // Définir l'alignement du texte au centre
    attrs.setAttribute(textAlign); // Assigner l'attribut d'alignement du texte aux attributs de structure

    // Créer un nouvel attribut de structure pour l'espace après l'élément
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(21.75); // Définir la valeur de l'espace après à 21,75 unités
    attrs.setAttribute(spaceAfter); // Assigner l'attribut d'espace après aux attributs de structure


    // Créer un nouvel élément SpanElement à ajouter à p2
    SpanElement span2 = tagged.createSpanElement();

    // Créer des attributs de structure pour l'élément span
    StructureAttributes attrs = span2.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Créer un nouvel attribut de structure pour le type de décoration du texte
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Définir la décoration du texte en soulignement
    attrs.setAttribute(textDecorationType); // Assigner l'attribut de type de décoration du texte aux attributs de structure

    // Créer un nouvel attribut de structure pour la couleur de la décoration du texte en utilisant la clé spécifiée.
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);

    // Définir la valeur numérique du tableau pour l'attribut de couleur de décoration du texte.
    // La couleur est représentée dans un tableau de valeurs RGB, où chaque valeur est un Double.
    textDecorationColor.setArrayNumberValue(new Double[][] {
    new Double[] { (0.0196075) }, // Composante rouge
    new Double[] { (0.384308) },  // Composante verte
    new Double[] { (0.756866) }   // Composante bleue
    });

    // Définir l'attribut de couleur de décoration du texte à l'objet attrs.
    attrs.setAttribute(textDecorationColor);

    // Ajouter un élément span enfant à l'élément parent p2.
    p2.appendChild(span2);

    // Créer une nouvelle instance de LinkElement pour le deuxième lien.
    LinkElement link2 = tagged.createLinkElement();

    // Assigner un identifiant unique à l'élément lien en utilisant un UUID généré aléatoirement.
    link2.setId(UUID.randomUUID().toString());

    // Ajouter l'élément link2 comme enfant de span2.
    span2.appendChild(link2);

    // Baliser l'élément link2 avec l'annotation correspondante des annotations de la page.
    link2.tag(page.getAnnotations().get_Item(1));

    // Baliser l'élément link2 avec des métadonnées supplémentaires ou un contexte (link2Bdc).
    link2.tag(link2Bdc);

    // Créer une autre instance de LinkElement pour le premier lien.
    LinkElement link1 = tagged.createLinkElement();

    // Assigner un identifiant unique à l'élément link1 en utilisant un UUID généré aléatoirement.
    link1.setId(UUID.randomUUID().toString());

    // Ajouter l'élément link1 comme enfant de span1.
    span1.appendChild(link1);

    // Baliser l'élément link1 avec l'annotation correspondante des annotations de la page.
    link1.tag(page.getAnnotations().get_Item(2));

    // Baliser l'élément link1 avec des métadonnées supplémentaires ou un contexte (link1Bdc).
    link1.tag(link1Bdc);

    // Supprimer le premier élément enfant de l'élément racine du document balisé.
    tagged.getRootElement().removeChild(0);

    // Enregistrer le document dans le répertoire de sortie spécifié avec le nom de fichier "_out.pdf".
    document.save(dataDir + "_out.pdf");

```


## Quoi de neuf dans Aspose.PDF 24.6

Depuis la version 24.6, Aspose.PDF pour Java permet de signer un PDF avec java.security.cert.X509Certificate, java.security.PrivateKey :

Ce code récupère un certificat et une clé privée depuis le magasin de certificats, puis les utilise pour appliquer une signature numérique à la première page d'un document PDF.

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

## Quoi de neuf dans Aspose.PDF 24.5

Depuis la version 24.5, les plugins de l'éditeur de formulaires ont été implémentés.

**Comment modifier des formulaires en PDF à l'aide de l'éditeur de formulaires**

- Définissez vos clés de licence
- Créez une instance de la classe FormEditor, qui fournit des méthodes pour manipuler les formulaires PDF
- Créez une instance de la classe FormEditorAddOptions, qui spécifie les options pour ajouter des champs de formulaire à un document PDF
- Ajoutez une source de fichier d'entrée et une source de fichier de sortie à l'objet FormEditorAddOptions, en utilisant la classe FileDataSource qui représente un chemin de fichier ou un flux
- Appelez la méthode Process de l'objet FormEditor, en passant l'objet FormEditorAddOptions en tant que paramètre
- Accédez au résultat en utilisant ResultContainer.resultCollection

```java

    // Spécifiez les chemins d'entrée et de sortie pour les fichiers PDF.
    String inputPath = "sample.pdf";
    String outputPath = "out.pdf";

    // Créez une instance du plugin FormEditor.
    FormEditor pdfFormPlugin = new FormEditor();

    // Créez des options pour ajouter des champs de formulaire.
    ArrayList<FormFieldCreateOptions> options = new ArrayList<FormFieldCreateOptions>();

    // Créez un champ de formulaire de zone de texte.
    FormTextBoxFieldCreateOptions tmp1 = new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 600, 90, 610));
    tmp1.setValue("TextBoxField");
    tmp1.setColor(Color.getChocolate());
    tmp1.setPartialName("TexBoxField");
    options.add(tmp1);

    // Créez un champ de formulaire de boîte combinée.
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

    // Créez un champ de formulaire de case à cocher.
    FormCheckBoxFieldCreateOptions tmp3 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715));
    tmp3.setValue("CheckBoxField 1");
    tmp3.setPartialName("CheckBoxField_1");
    tmp3.setColor(Color.getBlue());
    options.add(tmp3);


    // Créez un champ de formulaire de case à cocher.
    FormCheckBoxFieldCreateOptions tmp4 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(100, 700, 190, 715));
    tmp4.setChecked(new Boolean[]{true});
    tmp4.setValue("CheckBoxField 2");
    tmp4.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    tmp4.setStyle(new Integer[]{BoxStyle.Cross});
    options.add(tmp4);


    // Créez un champ de formulaire de case à cocher.
    FormCheckBoxFieldCreateOptions tmp5 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(200, 700, 390, 715));
    tmp5.setPartialName("CheckBoxField_3");
    tmp5.setValue("CheckBoxField 3");
    tmp5.setStyle(new Integer[]{BoxStyle.Star});
    tmp5.setChecked(new Boolean[]{true});
    tmp5.setTextHorizontalAlignment(new HorizontalAlignment[]{HorizontalAlignment.Center});
    options.add(tmp5);

    FormEditorAddOptions opt = new FormEditorAddOptions(options);

    // Ajoutez les fichiers d'entrée et de sortie aux options.
    opt.addInput(new FileDataSource(inputPath));
    opt.addOutput(new FileDataSource(outputPath));

    // Traitez les champs de formulaire à l'aide du plugin.
    ResultContainer results = pdfFormPlugin.process(opt);
```


Cette version nous permet de travailler avec des calques PDF. Par exemple :

- verrouiller un calque PDF
- extraire les éléments d'un calque PDF
- aplatir un PDF à calques
- fusionner tous les calques dans le PDF en un seul

**Verrouiller un calque PDF**

Depuis la version 24.5, vous pouvez ouvrir un PDF, verrouiller un calque spécifique sur la première page et enregistrer le document avec les modifications. Deux nouvelles méthodes et une propriété ont été ajoutées :

Layer.Lock(); - Verrouille le calque.
Layer.Unlock(); - Déverrouille le calque.
Layer.Locked; - Propriété, indiquant l'état de verrouillage du calque.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    Layer layer = page.getLayers().get(0);

    layer.lock();

    document.save(output);
```

**Extraire les éléments d'un calque PDF**

La bibliothèque Aspose.PDF pour Java permet d'extraire chaque calque de la première page et d'enregistrer chaque calque dans un fichier séparé.

Pour créer un nouveau PDF à partir d'un calque, le code suivant peut être utilisé :

```java

    Document document = new Document(inputPath);
    java.util.List<Layer> layers = document.getPages().get_Item(1).getLayers();

    for (Layer layer : layers)
    {
        layer.save(outputPath);
    }
```


**Aplatir un PDF à couches**

La bibliothèque Aspose.PDF pour Java ouvre un PDF, parcourt chaque couche de la première page et aplatit chaque couche, la rendant permanente sur la page.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);

    for (Layer layer : page.getLayers())
    {
        layer.flatten(true);
    }
    document.save(output);
```

La méthode Layer.flatten(boolean cleanupContentStream) accepte le paramètre booléen qui spécifie s'il faut supprimer les marqueurs de groupes de contenu optionnels du flux de contenu. Définir le paramètre cleanupContentStream à false accélère le processus d'aplatissement.

**Fusionner toutes les couches à l'intérieur du PDF en une seule**

La bibliothèque Aspose.PDF pour Java permet de fusionner soit toutes les couches PDF, soit une couche spécifique sur la première page dans une nouvelle couche et enregistre le document mis à jour.

Deux méthodes ont été ajoutées pour fusionner toutes les couches sur la page :

- void mergeLayers(String newLayerName);

- void mergeLayers(String newLayerName, String newOptionalContentGroupId);

Le deuxième paramètre permet de renommer le marqueur de groupe de contenu optionnel. La valeur par défaut est "oc1" (/OC /oc1 BDC).

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    page.mergeLayers("NewLayerName");

    // Ou page.mergeLayers("NewLayerName", "OC1");

    document.save(output);
```

## Quoi de neuf dans Aspose.PDF 24.4

Cette version a introduit des plugins Java pour PDF :

- Plugin de Flattening de Formulaire

```java

    FormFlattener pdfFormPlugin = new FormFlattener();

    FormFlattenAllFieldsOptions opt = new FormFlattenAllFieldsOptions();

    opt.addInput(new FileDataSource("sample.pdf"));
    opt.addOutput(new FileDataSource("sample-flat.pdf"));

    ResultContainer result = pdfFormPlugin.process(opt);

    // Vérifier le résultat.
    java.util.List < IOperationResult > resultCollectionInternal = result.getResultCollection();
```

- Exportateur de Formulaire

```java

    Rectangle rect = new com.aspose.pdf.Rectangle(0, 220, 600, 330);

    // Utilisation du plugin.
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

    // Vérifier le résultat.
    System.out.println(result.getResultCollectionInternal().size() > 0);
    System.out.println(result.getResultCollectionInternal().get_Item(0).isFile());
    System.out.println(result.getResultCollectionInternal().get_Item(0).getData().toString());
```


- Plugin de Fusion

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

- Plugin d'Optimisation

Comment réduire la taille des documents PDF ?

```java

    String input = "Test.pdf";
    String output = "Optimized.pdf";

    Optimizer optimizer = new Optimizer();

    OptimizeOptions opt = new OptimizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    optimizer.process(opt);
```

Comment redimensionner les documents PDF ?

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


Comment faire pivoter des documents PDF ?

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

## Quoi de neuf dans Aspose.PDF 24.3

À partir de 24.3, implémentez une recherche à travers une liste de phrases dans un TextFragmentAbsorber.

```java

    String[] expressions = new String[] {
      //détecter le numéro de téléphone
      "\\b\\d{3}-\\d{3}-\\d{4}\\b",
      //détecter le numéro de carte
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


La prochaine fonctionnalité est d'ajouter la capacité de convertir des tableaux pour le convertisseur PDF vers Markdown

```java

    Document doc = new Document(dataDir + "56201.pdf");
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    doc.save(dataDir + "56201.md", saveOptions);
```

## Quoi de neuf dans Aspose.PDF 24.2

À partir de la version 24.2, il est possible d'ajouter le filigrane dans le PDF avec AcroForms. TextStamp est adapté pour une utilisation avec les fichiers AcroForm. Si vous utilisez TextStamp pour les fichiers XFA, le texte est dessiné sur la page comme dans un fichier PDF habituel (il peut être vu dans ces visionneuses PDF qui ne peuvent pas lire les fichiers XFA, par exemple, dans un navigateur Chrome). Pour ajouter du texte au fichier XFA, il doit être modifié dans le XML interne du fichier XFA.

```java

    String sourceName = dataDir + "551.3xfa.pdf";
    String targetName = dataDir + "output_2_" + BuildVersionInfo.AssemblyVersion + ".pdf";

    Document pdfDocument = new Document(sourceName);
    XFA xfa = pdfDocument.getForm().getXFA();

    String watermark =
    "<subform>" +
    "<draw rotate=\"90\" x=\"100px\" y=\"100px\">" +
    "<value>" +
    "<text>Exemple de tampon</text>\n" +
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


Définir StateModel pour Annotation  
Nous pouvons utiliser setReviewState et setMarkedState de la classe MarkupAnnotation pour définir l'état nécessaire.  
Toutes les annotations de marquage ont une option Définir l'état disponible.

```java

    // Ouvrir le document PDF source
    Document pdfDocument = new Document();
    pdfDocument.getPages().add();
    // Créer une annotation
    TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.getPages().get_Item(1), new Rectangle(200,
            400, 400, 600));

    //Définir le titre de l'annotation
    textAnnotation.setTitle("Titre d'annotation d'exemple");

    //Définir le sujet de l'annotation
    textAnnotation.setSubject("Sujet d'exemple");
    //Spécifier le contenu de l'annotation
    textAnnotation.setContents("Contenu d'exemple pour l'annotation");
    textAnnotation.setOpen(true);
    textAnnotation.setIcon(TextIcon.Key);
    com.aspose.pdf.Border border = new com.aspose.pdf.Border(textAnnotation);
    border.setWidth(5);
    border.setDash(new Dash(1, 1));
    textAnnotation.setBorder(border);
    String userName1 = "Aspose1";
    textAnnotation.setReviewState(AnnotationState.Rejected, userName1);
    textAnnotation.setRect(new Rectangle(200, 400, 400, 600));

    //Ajouter l'annotation dans la collection d'annotations de la page
    pdfDocument.getPages().get_Item(1).getAnnotations().add(textAnnotation);
    pdfDocument.processParagraphs();

    //Enregistrer le fichier de sortie
    pdfDocument.save(dataDir + "output_24_2_Rejected.pdf");

    pdfDocument = new Document(dataDir + "output" + version + "3.pdf");
    TextAnnotation textAnnotation2 = (TextAnnotation) pdfDocument.getPages().get_Item(1).getAnnotations().get_Item(1);

    String userName2 = "Aspose2";
    textAnnotation2.setReviewState(AnnotationState.Accepted, userName2);
    pdfDocument.save(dataDir + "output_24_2_Rejected_and_Accepted.pdf");
```


À partir de la version 24.2, implémenter la conversion OFD en PDF :

```java

    Document document = new Document(inputPath, new OfdLoadOptions());
    document.save(outputPath);
```

## Quoi de neuf dans Aspose.PDF 24.1

À partir de la version 24.1, implémenter la conversion PDF en Markdown :

```java

    final Document doc = new Document(inputPdfPath);
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Outlines);
    doc.save(markdownOutputFilePath, saveOptions);
```

Également, dans la version 24.1, l'interruption de thread en utilisant l'InterruptMonitor a été implémentée.

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

          topicRow.getCells().add("texte");
          topicRow.getCells().add("texte");
          topicRow.getCells().add("texte");
          topicRow.getCells().add("texte");
          topicRow.getCells().add("texte");
          topicRow.getCells().add("texte");

          // Conversion des instructions foreach en while
          Iterator tmp0 = (topicRow.getCells()).iterator();
          while (tmp0.hasNext()) {
            Cell cell = (Cell) tmp0.next();
            cell.setVerticalAlignment(VerticalAlignment.Center);
            cell.setAlignment(HorizontalAlignment.Center);
          }

          Row row2 = topicTable.getRows().add();
          row2.getCells().add("texte");
          row2.getCells().add("texte");
          row2.getCells().add("texte");
          String LongText = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.";
          row2.getCells().add(LongText);
          row2.getCells().add("texte");
          row2.getCells().add("texte");
          page.getParagraphs().add(topicTable);
          document.save(dataDir + "out" + version + ".pdf");

        } catch (com.aspose.pdf.exceptions.OperationCanceledException ex) {
          System.out.println("Interruption du thread de sauvegarde à " + System.currentTimeMillis());
        } finally {
          if (document != null) {
            document.close();
          }
        }

      }

    }).start();

    System.out.println("Le processus a démarré le thread à " + System.currentTimeMillis());

    // Le délai d'attente doit être inférieur au temps nécessaire pour l'enregistrement complet du document (sans interruption).
    Thread.sleep(500);

    // Interrompre le processus
    monitor.interrupt();

    System.out.println("Thread de sauvegarde interrompu à " + System.currentTimeMillis());
```


## Quoi de neuf dans Aspose.PDF 23.12

Le formulaire peut être trouvé et le texte peut être remplacé en utilisant le fragment de code suivant :

```java

    Document document = new Document(input);
    String expectedText = "Ceci est un texte ajouté lors de la création d'un nouveau PDF dans Kofx Power PDF Standard.";

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

Ou, le formulaire peut être complètement supprimé :

```java

    Document document = new Document(input);
    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    //conversion des déclarations foreach à while
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


Une autre variante de suppression du formulaire :

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

- Tous les formulaires peuvent être supprimés en utilisant l'extrait de code suivant :

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    forms.clear();

    document.save(output);
```

## Quoi de neuf dans Aspose.PDF 23.11

À partir de cette version, il est possible de supprimer le texte caché d'un fichier PDF :

```java

    Document document = new Document(inputFile);

    TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
    textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
    document.getPages().accept(textAbsorber);

    msStringBuilder result = new msStringBuilder();

    // Conversion de foreach à des instructions while
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


## Quoi de neuf dans Aspose.PDF 23.10

La mise à jour actuelle présente trois versions de la suppression des balises des PDF balisés.

- Supprimer un élément de nœud d'un documentElement (élément racine de l'arbre) :

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element documentElement = structure.getChildren().get_Item(0);
    Element structElement = (documentElement.getChildren().getCount() > 1) ?  documentElement.getChildren().get_Item(1) : null;
    documentElement.getChildren().remove(structElement);
    // Vous pouvez également supprimer le structElement lui-même
                //if (structElement != null)
                //{
                //    structElement.remove();
                //}
    document.save(outputPath);
```

- Supprimer toutes les balises d'éléments marquées du document, mais conserver les éléments de structure :

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


- Supprimer toutes les balises :

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root = structure.getChildren().get_Item(0);
    root.remove();
    document.save(outputPath);
```

Nous avons implémenté une nouvelle fonctionnalité pour mesurer la hauteur des caractères. Utilisez le code suivant pour mesurer la hauteur d'un caractère :

```java

    Document doc = new Document("input.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.visit(doc.getPages().get_Item(1));
    double height = absorber.getTextFragments().get_Item(1).getTextState().measureHeight('h')
```

Notez que la mesure est basée sur la police intégrée dans le document. Si des informations relatives à une dimension manquent, cette méthode retourne 0.

## Quoi de neuf dans Aspose.PDF 23.9

À partir de 23.9, support pour supprimer une annotation enfant d'un champ remplissable.

exemple 1 :

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
    String option1 = "option 1";
    String option2 = "option 2";
    String outputPdf = "output.pdf";

    final Document document = new Document();
    try /*JAVA: utilisait*/ {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

        // Définir la valeur de l'option du premier groupe de cases à cocher
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


Ajouter une image avec ImageFilterType.Flate ne préserve pas la transparence.

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

## Quoi de neuf dans Aspose.PDF 23.8

La fonction de détection des mises à jour incrémentielles dans un document PDF a été ajoutée dans la version 23.8. Cette fonction renvoie 'true' lorsque le document a été enregistré avec des mises à jour incrémentielles, sinon elle renvoie 'false'.

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
     
Une autre fonctionnalité est la copie des OutputIntents du PDF source vers le PDF de destination.

Nous ajoutons une nouvelle propriété publique Document.getOutputIntents() pour permettre l'accès aux intentions de sortie dans un document. Pour le moment, seule l'utilisation des intentions de sortie déjà existantes dans certains documents est prise en charge, l'utilisateur ne peut pas créer une OutputIntent à partir de zéro.

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


De Aspose.PDF 23.8 prise en charge pour ajouter l'extraction de forme :

```java

{
    String input1 = getInputPdf("46298_1");
    String input2 = getInputPdf("46298_2");

    Document source = new Document(input1);
    Document dest = new Document(input2);

    Page destPage = dest.getPages().get_Item(1);

    TextFragmentAbsorber tfAbsorber = new TextFragmentAbsorber();
    tfAbsorber.visit(source.getPages().get_Item(1));

    //conversion foreach à while
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

        // Recalculer une nouvelle position car la taille de la page diffère du PDF original
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


Aussi prend en charge la capacité de détecter le débordement lors de l'ajout de texte :

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


## Quoi de neuf dans Aspose.PDF 23.7

À partir de la version 23.7, prise en charge des préréglages de mise à l'échelle de la page dans la boîte de dialogue d'impression :

```java

    Document document = new Document();
    document.getPages().add();
    document.setPrintScaling(PrintScaling.None);//PrintScaling.Default
    document.save(outputPdf);

    Document documentOutput = new Document(outputPdf);
    int printScaling = documentOutput.getPrintScaling();
    System.out.println("PrintScaling: " + printScaling);
```

## Quoi de neuf dans Aspose.PDF 23.6

À partir de la version 23.6, prise en charge de la possibilité de définir le titre de la page HTML, Epub.

code pour HTML :

```java

    HtmlSaveOptions options = new HtmlSaveOptions();
    options.setFixedLayout(true);
    options.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
    options.setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml);
    options.setTitle("</title>NOUVELLE PAGE & TITRE</head>");

    Document document = new Document(inputPath);
    document.save(outPath, options);
```


code pour EPUB :

```java

    EpubSaveOptions epubSaveOptions = new EpubSaveOptions();
    epubSaveOptions.setTitle("</title>NOUVELLE PAGE & TITRE</head>");
    epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

    Document document = new Document(inputPath);
    document.save(outPath, epubSaveOptions);
```

À partir de 23.6, support pour fournir une API pour le positionnement des graphiques vectoriels :

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

## Quoi de neuf dans Aspose.PDF 23.1

À partir de la version 23.1, prise en charge de la création d'une annotation PrinterMark. Ajout de l'une des variantes d'annotation : ColorBarAnnotation.

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


## Quoi de neuf dans Aspose.PDF 22.12

À partir de cette version, prise en charge de la conversion de PDF en image DICOM :

```java

    DicomDevice device = new DicomDevice(PageSize.getA4());
    Document doc = new Document("Input.pdf");
    ByteArrayOutputStream stream = new ByteArrayOutputStream();
    device.process(doc.getPages().get_Item(1), stream);
```

## Quoi de neuf dans Aspose.PDF 22.9

À partir de la version 22.09, support pour l'ajout d'une propriété permettant de modifier l'ordre des rubriques de sujet (E=, CN=, O=, OU=,) dans la signature.

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

## Quoi de neuf dans Aspose.PDF 22.8

À partir de Aspose.PDF 23.8, support pour ajouter une méthode pour reconstruire la table xref :

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

## Quoi de neuf dans Aspose.PDF 22.6

PDF en PDF_A_1A - mettre en œuvre une option pour supprimer la couleur de transparence afin d'éviter une grande taille de fichier de sortie.

À partir de la version 22.5, le client est capable de contrôler la qualité de la transparence convertie, et la taille du fichier de sortie en conséquence :

```java
    opts.setTransparencyResolution(300);
```

## Quoi de neuf dans Aspose.PDF 22.5

Lors de la conversion PDF/A, le contenu transparent est supprimé et remplacé par une image.
Nous avons mis en œuvre une nouvelle fonctionnalité, et maintenant le client peut contrôler la qualité de l'image avec le paramètre TransparencyResolution :

```java

    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
    PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
    options.setTransparencyResolution(300);
    pdfDocument.convert(options);
    pdfDocument.save("finalOutput.pdf");
```


## Quoi de neuf dans Aspose.PDF 22.4

Cette version inclut des informations pour Aspose.PDF pour Java :

- PDF vers ODS : Reconnaître le texte en indice et exposant ;

**exemple**

```java

    Document pdfDocument = new Document("Superscript-Subscript.pdf");
    ExcelSaveOptions options = new ExcelSaveOptions();
    options.Format = ExcelSaveOptions.ExcelFormat.ODS;
    pdfDocument.Save("output.ods"), options);
```

- PDF vers XMLSpreadSheet2003 : Reconnaître le texte en indice et exposant ;

- PDF vers Excel : Reconnaître le texte en indice et exposant ;

## Quoi de neuf dans Aspose.PDF 22.3

PDF vers ODS : Le support pour RTL est disponible dans la version 22.3

```java

    ExcelSaveOptions options = new ExcelSaveOptions();
    options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
    pdfDocument.save("output.ods", options);
```

## Quoi de neuf dans Aspose.PDF 22.2

Cette version inclut le PDF vers XSLX : Support pour RTL (Hébreu, Arabe).

## Quoi de neuf dans Aspose.PDF 22.1

Aspose.PDF pour Java permet de charger des documents au format Portable Document Format (PDF) version 2.0.

## Quoi de neuf dans Aspose.PDF 21.10

### Comment détecter le texte caché ?

Veuillez utiliser le code suivant :

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


## Quoi de neuf dans Aspose.PDF 21.8

### Comment changer la couleur du texte dans la signature numérique ?

Dans la version 21.8, setForegroundColor permet de changer la couleur du texte dans la signature numérique :

```java
Veuillez utiliser le code suivant :

                    PdfFileSignature pdfSign = new PdfFileSignature();                
                    pdfSign.bindPdf(inFile);
                    // créer un rectangle pour l'emplacement de la signature
                    java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);
                    PKCS7 pkcs = new PKCS7(inPfxFile, "");

                    pkcs.setCustomAppearance( new SignatureCustomAppearance());
// définir la couleur du texte
                    pkcs.getCustomAppearance().setForegroundColor(Color.getGreen());

                    // signer le fichier PDF
                    pdfSign.sign(1, true, rect, pkcs);
                    // sauvegarder le fichier PDF de sortie
                    pdfSign.save(outFile);
```

## Quoi de neuf dans Aspose.PDF 21.6

### Masquer une image en utilisant ImagePlacementAbsorber du document

Avec Aspose.PDF pour Java, vous pouvez masquer des images en utilisant ImagePlacementAbsorber depuis le document :

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

## Quoi de neuf dans Aspose.PDF 21.5

### Ajouter une API pour fusionner des images

Aspose.PDF 21.4 vous permet de combiner des images. Fusionne une liste de flux d'images en un seul flux d'image. Les formats de sortie Png/jpg/tiff sont pris en charge, en cas d'utilisation d'un format non pris en charge, le flux de sortie est encodé par défaut en Jpeg.
Suivez l'extrait de code suivant :

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


Aussi, vous pouvez fusionner vos images au format Tiff :

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

## Quoi de neuf dans Aspose.PDF 21.02

Aspose.PDF v21.02 Signer un PDF avec des signatures PAdES LTV

```java
final Document document = new Document(inputPdf);
    try 
    {
        PdfFileSignature signature = new PdfFileSignature(document);
        PKCS7 pkcs7 = new PKCS7(getInputPath("cert.pfx"), "password");
        //Signer le PDF avec des signatures PAdES LTV
        pkcs7.setUseLtv(true);

        signature.sign(1, true, new Rectangle(100, 100, 300, 300), pkcs7);
        signature.save(outputPdf);
    }
    finally { if (document != null) (document).dispose(); }
```