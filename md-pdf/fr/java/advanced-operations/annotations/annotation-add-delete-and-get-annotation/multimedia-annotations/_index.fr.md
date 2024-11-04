---
title: Annotation Multimédia PDF 
linktitle: Annotation Multimédia
type: docs
weight: 40
url: /java/multimedia-annotation/
description: Aspose.PDF pour Java vous permet d'ajouter, obtenir et supprimer l'annotation multimédia de votre document PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les annotations dans un document PDF sont contenues dans la collection Annotations d'un objet [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page). Cette collection contient toutes les annotations pour cette page individuelle uniquement : chaque page a sa propre collection Annotations. Pour ajouter une annotation à une page particulière, ajoutez-la à la collection Annotations de cette page en utilisant la méthode Add.

Utilisez la classe [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/ScreenAnnotation) dans l'espace de noms Aspose.PDF.InteractiveFeatures.Annotations pour inclure des fichiers SWF en tant qu'annotations dans un document PDF à la place.
 Une annotation d'écran spécifie une région d'une page sur laquelle des clips multimédias peuvent être joués.

Lorsque vous devez ajouter un lien vidéo externe dans un document PDF, vous pouvez utiliser [MovieAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/MovieAnnotation). Une annotation de film contient des graphiques animés et du son à présenter sur l'écran de l'ordinateur et à travers les haut-parleurs.

Une [annotation sonore](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation) doit être analogue à une annotation de texte, sauf qu'au lieu d'une note de texte, elle contient du son enregistré à partir du microphone de l'ordinateur ou importé d'un fichier. Lorsque l'annotation est activée, le son doit être joué. L'annotation doit se comporter comme une annotation de texte de la plupart des manières, avec une icône différente (par défaut, un haut-parleur) pour indiquer qu'elle représente un son.

Cependant, lorsqu'il est nécessaire d'intégrer des médias à l'intérieur d'un document PDF, vous devez utiliser [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/RichMediaAnnotation).
Les méthodes/propriétés suivantes de la classe RichMediaAnnotation peuvent être utilisées.

- Stream CustomPlayer { set; }: Permet de définir le lecteur utilisé pour lire la vidéo.
- string CustomFlashVariables { set; }: Permet de définir des variables qui sont passées à l'application flash. Cette ligne est un ensemble de paires “key=value” qui sont séparées par ‘&'.
- void AddCustomData(strig name, Stream data):  Ajouter des données supplémentaires pour le lecteur. Par exemple source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}:  L'événement active le lecteur ; les valeurs possibles sont Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Définir les données vidéo/audio à lire.
- void Update():  Créer une structure de données de l'annotation. Cette méthode doit être appelée en dernier
- void SetPoster(Stream): Définir l'affiche de la vidéo, c'est-à-dire l'image affichée lorsque le lecteur n'est pas actif

## Ajouter une Annotation d'Écran

L'extrait de code suivant montre comment ajouter une annotation d'écran à un fichier PDF :

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;
import com.aspose.pdf.*;

public class ExampleMultimediaAnnotation {

    // Le chemin vers le répertoire des documents.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddScreenAnnotation() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "input.swf";
        // Créer une annotation d'écran
        ScreenAnnotation screenAnnotation = new ScreenAnnotation(page, new Rectangle(170, 190, 470, 380), mediaFile);
        page.getAnnotations().add(screenAnnotation);

        document.save(_dataDir + "sample_swf.pdf");
    }
}
```


## Ajouter une Annotation Sonore

Le code suivant montre comment ajouter une annotation sonore à un fichier PDF :

```java
          public static void AddSoundAnnotation() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "file_example_WAV_1MG.wav";

        // Créer une annotation sonore
        SoundAnnotation soundAnnotation = new SoundAnnotation(page, new Rectangle(20, 700, 60, 740), mediaFile);
        soundAnnotation.setColor(Color.getBlue());
        soundAnnotation.setTitle("John Smith");
        soundAnnotation.setSubject("Démonstration d'annotation sonore");
        soundAnnotation.setPopup(new PopupAnnotation(document));

        page.getAnnotations().add(soundAnnotation);

        document.save(_dataDir + "sample_wav.pdf");
    }
```

## Ajouter une RichMediaAnnotation

Le code suivant montre comment ajouter une RichMediaAnnotation à un fichier PDF :

```java
     public static void AddRichMediaAnnotation() throws FileNotFoundException {
        Document doc = new Document();
        var pathToAdobeApp = "C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";
        Page page = doc.getPages().add();

        // donner un nom aux données vidéo. Ces données seront intégrées dans le document avec ce
        // nom et référencées à partir des variables flash par ce nom.
        // videoName ne doit pas contenir le chemin vers le fichier ; c'est plutôt une "clé" pour accéder
        // aux données à l'intérieur du document PDF

        String videoName = "file_example_MP4_480_1_5MG.mp4";
        String posterName = "file_example_MP4_480_1_5MG_poster.jpg";

        // nous utilisons également un skin pour le lecteur vidéo
        String skinName = "SkinOverAllNoFullNoCaption.swf";

        RichMediaAnnotation rma = new RichMediaAnnotation(page, new Rectangle(100, 500, 300, 600));

        // ici, nous devons spécifier le flux contenant le code du lecteur vidéo
        rma.setCustomPlayer(new FileInputStream(pathToAdobeApp + "Players" + "Videoplayer.swf"));

        // composer la ligne de variables flash pour le lecteur. veuillez noter que différents lecteurs
        // peuvent avoir un format différent de la ligne de variables flash.
        // Consultez la documentation de votre lecteur.
        rma.setCustomFlashVariables("source=" + videoName + "&skin=" + skinName);

        // ajouter le code du skin.
        rma.addCustomData(skinName, new FileInputStream(pathToAdobeApp + "SkinOverAllNoFullNoCaption.swf"));
        // définir l'affiche pour la vidéo
        rma.setPoster(new FileInputStream(_dataDir + posterName));

        // définir le contenu vidéo
        rma.setContent(videoName, new FileInputStream(_dataDir + videoName));

        // définir le type de contenu (vidéo)
        rma.setType(RichMediaAnnotation.ContentType.Video);

        // activer le lecteur par clic
        rma.setActivateOn(RichMediaAnnotation.ActivationEvent.Click);

        // mettre à jour les données de l'annotation. Cette méthode doit être appelée après toutes les
        // affectations/configurations. Cette méthode initialise la structure de données de l'annotation
        // et intègre les données requises.
        rma.update();

        // ajouter l'annotation sur la page.
        page.getAnnotations().add(rma);

        doc.save(_dataDir + "RichMediaAnnotation.pdf");
    }
```


## Obtenir MultimediaAnnotation

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir MultimediaAnnotation à partir d'un document PDF.

```java
public static void GetMultimediaAnnotation() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();

        for (Annotation ma : mediaAnnotations) {
            System.out.println(ma.getAnnotationType() + " " + ma.getRect());
        }
    }
```

## Supprimer MultimediaAnnotation

L'extrait de code suivant montre comment supprimer MultimediaAnnotation d'un fichier PDF.

```java
    public static void DeletePolyAnnotation() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();
        for (Annotation ma : mediaAnnotations) {
            page.getAnnotations().delete(ma);
        }
        document.save(_dataDir + "RichMediaAnnotation_del.pdf");
    }
```


## Ajouter des Annotations de Widget

Les formulaires interactifs utilisent les [Annotations de Widget](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/WidgetAnnotation) pour représenter l'apparence des champs et gérer les interactions utilisateur. Nous utilisons ces éléments de formulaire ajoutés à un PDF pour faciliter l'entrée, la soumission d'informations, ou effectuer d'autres interactions utilisateur.

Les Annotations de Widget sont une représentation graphique d'un champ de formulaire sur des pages spécifiques, donc nous ne pouvons pas les créer directement en tant qu'annotation.

Chaque Annotation de Widget aura des graphiques appropriés (apparence) en fonction de son type. Après la création, certains aspects visuels peuvent être modifiés, tels que le style de bordure et la couleur de fond. D'autres propriétés, telles que la couleur du texte et la police, peuvent être modifiées via le champ, une fois attaché à celui-ci.

Dans certains cas, vous pouvez vouloir qu'un champ apparaisse sur plus d'une page, répétant la même valeur.
 Dans ce cas, les champs qui ont normalement un seul widget peuvent avoir plusieurs widgets attachés : un TextField, ListBox, ComboBox et CheckBox ont généralement exactement un, tandis que le RadioGroup a plusieurs widgets, un pour chaque bouton radio.  
Quelqu'un remplissant le formulaire peut utiliser n'importe lequel de ces widgets pour mettre à jour la valeur du champ, et cela est reflété dans tous les autres widgets également.

Chaque champ de formulaire pour chaque endroit dans le document représente une Annotation de Widget. Les données spécifiques à la localisation de l'Annotation de Widget sont ajoutées à la page particulière. Chaque champ de formulaire a plusieurs variations. Un bouton peut être un bouton radio, une case à cocher ou un bouton poussoir. Un widget de choix peut être une boîte de liste ou une boîte combinée.

Dans cet exemple, nous allons apprendre comment ajouter des boutons poussoirs pour la navigation dans le document.

## Ajouter un bouton au document

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWidgetAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddButton()
    {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        Rectangle rect = new Rectangle(72, 748, 164, 768);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Imprimer le document actuel");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setNormalCaption("Imprimer le document");

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);

        printButton.setBorder(border);
        printButton.getCharacteristics().setBorder(Color.fromArgb(255, 0, 0, 255));
        printButton.getCharacteristics().setBackground(Color.fromArgb(255, 0, 191, 255));
        document.getForm().add(printButton);

        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

Ce bouton a une bordure et un fond. Nous avons également défini un nom de bouton (Name), une info-bulle (AlternateName), une étiquette (NormalCaption), et une couleur pour le texte de l'étiquette (Color).

## Utilisation des actions de navigation dans le document

Il existe un exemple plus complexe de l'utilisation des annotations de widget - la navigation dans le document PDF. Cela peut être nécessaire pour préparer une présentation de document PDF.

Cet exemple montre comment créer 4 boutons :

```java
public static void AddDocumentNavigationActions() {
// Charger le fichier PDF
Document document = new Document(_dataDir + "JSON Fundamenals.pdf");

ButtonField[] buttons = new ButtonField[4];
String[] alternateNames = { "Aller à la première page", "Aller à la page précédente", "Aller à la page suivante", "Aller à la dernière page" };
String[] normalCaptions = { "Premier", "Précédent", "Suivant", "Dernier" };
int[] actions = { PredefinedAction.FirstPage, PredefinedAction.PrevPage, PredefinedAction.NextPage,
PredefinedAction.LastPage };
Color clrBorder = Color.fromArgb(255, 0, 255, 0);
Color clrBackGround = Color.fromArgb(255, 0, 96, 70);

for (int i = 0; i < 4; i++) {
buttons[i] = new ButtonField(document, new Rectangle(32 + i * 80, 28, 104 + i * 80, 68));
buttons[i].setAlternateName(alternateNames[i]);
buttons[i].setColor(Color.getWhite());
buttons[i].setNormalCaption(normalCaptions[i]);
buttons[i].setOnActivated(new NamedAction(actions[i]));
Border border = new Border(buttons[i]);
border.setStyle(BorderStyle.Solid);
border.setWidth(2);
buttons[i].setBorder(border);
buttons[i].getCharacteristics().setBorder(clrBorder);
buttons[i].getCharacteristics().setBackground(clrBackGround);
}

for (int pageIndex = 1; pageIndex <= 1; pageIndex++)
for (int i = 0; i < 4; i++)
document.getForm().add(buttons[i], "btn" + pageIndex + "_" + (i + 1), pageIndex);

document.getForm().get("btn1_1").setReadOnly(true);
document.getForm().get("btn1_2").setReadOnly(true);

document.getForm().get("btn" + document.getPages().size() + "_3").setReadOnly(true);
document.getForm().get("btn" + document.getPages().size() + "_4").setReadOnly(true);
document.save(_dataDir + "sample_widgetannot_2.pdf");
}
```


## Comment supprimer une annotation de widget

Aspose.PDF pour Java a des règles pour supprimer des annotations de votre fichier :

```java
public static void DeleteWidgetAnnotation() {
        // Charger le fichier PDF
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // Filtrer les annotations à l'aide de AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(new ButtonField(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> buttonFields = annotationSelector.getSelected();

        // supprimer les annotations
        for (Annotation wa : buttonFields) {
            page.getAnnotations().delete(wa);
        }
        document.save(_dataDir + "sample_widgetannot_del.pdf");
    }
```

Dans les documents PDF, vous pouvez visualiser et gérer du contenu 3D de haute qualité créé avec un logiciel de CAO 3D ou de modélisation 3D et intégré dans le document PDF.
 Peut faire pivoter des éléments 3D dans toutes les directions comme si vous les teniez dans vos mains.

Pourquoi avez-vous besoin d'un affichage 3D des images ?

Au cours des dernières années, la technologie a fait d'énormes progrès dans tous les domaines grâce à l'impression 3D. Les technologies d'impression 3D peuvent être appliquées pour enseigner des compétences technologiques dans la construction, le génie mécanique, le design en tant qu'outil principal. Ces technologies, grâce à l'émergence de dispositifs d'impression personnels, peuvent contribuer à l'introduction de nouvelles formes d'organisation du processus éducatif, augmenter la motivation et la formation des compétences nécessaires des diplômés et des enseignants.

La tâche principale de la modélisation 3D est l'idée d'un futur objet ou objet car, pour libérer un objet, vous avez besoin d'une compréhension de ses caractéristiques de conception dans tous les détails pour une régénération successive dans le design industriel ou l'architecture.

## Ajouter une annotation 3D

L'annotation 3D est ajoutée à l'aide d'un modèle créé au format U3D avec Aspose.PDF pour Java
1. Créez un nouveau [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)  
1. Chargez les données du modèle 3D souhaité (dans notre cas "Ring.u3d") pour créer [PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PDF3DContent)  
1. Créez un objet [3dArtWork](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DArtwork) et liez-le au document et au 3DContent  
1. Réglez l'objet pdf3dArtWork :  

    - 3DLightingScheme - (nous allons définir `CAD` dans l'exemple)
    - 3DRenderMode - (nous allons définir `Solid` dans l'exemple)
    - Remplissez `ViewArray`, créez au moins une [3D View](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DView) et ajoutez-la au tableau.

1. Définissez 3 paramètres de base dans l'annotation :
    - la `page` sur laquelle l'annotation sera placée,
    - le `rectangle`, à l'intérieur duquel se trouve l'annotation,
    - et l'objet `3dArtWork`.
1. Pour une meilleure présentation de l'objet 3D, définissez le cadre de la bordure  
1. Définissez la vue par défaut (par exemple - TOP)  

1. Ajoutez quelques paramètres supplémentaires : nom, affiche de prévisualisation, etc.
1. Ajoutez une annotation à la [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)
1. Sauvegardez le résultat

## Exemple

Veuillez vérifier l'extrait de code suivant pour ajouter une annotation 3D.

```java
    public class Example3DAnnotation
    {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";
    public static void Add3dAnnotation()
    {
    // Chargez le fichier PDF
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
    pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
    pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.getPages().add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
    pdf3dAnnotation.setDefaultViewIndex(1);
    pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
    pdf3dAnnotation.setName("Ring.u3d");
    //définir l'image de prévisualisation si nécessaire
    //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
    document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

    document.save(_dataDir+"sample_3d.pdf");
    }
}
```


This code example showed us such a model:

![3D Annotation demo](3d_demo.png)

Cet exemple de code nous a montré un tel modèle :