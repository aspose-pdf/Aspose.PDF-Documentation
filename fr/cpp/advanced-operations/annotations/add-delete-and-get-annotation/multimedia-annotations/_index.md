---
title: Annotation Multimédia PDF en C++
linktitle: Annotation Multimédia
type: docs
weight: 40
url: /fr/cpp/multimedia-annotation/
description: Aspose.PDF pour C++ vous permet d'ajouter, d'obtenir et de supprimer l'annotation multimédia de votre document PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Ajouter du contenu vidéo, audio et interactif transforme les PDFs en outils de communication multidimensionnels qui augmentent l'intérêt et l'engagement avec vos documents. Un tel contenu dans les fichiers au format PDF est appelé Annotations Multimédia.

Les annotations dans un document PDF sont contenues dans la collection Annotations d'un objet [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). Cette collection contient toutes les annotations pour cette page individuelle uniquement : chaque page a sa propre collection Annotations. Pour ajouter une annotation à une page particulière, ajoutez-la à la collection Annotations de cette page en utilisant la méthode Add.

Utilisez la classe [ScreenAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.screen_annotation) dans l'espace de noms Aspose.PDF.InteractiveFeatures.Annotations pour inclure des fichiers SWF comme annotations dans un document PDF. Une annotation d'écran spécifie une région d'une page sur laquelle des clips multimédias peuvent être joués.

Lorsque vous devez ajouter un lien vidéo externe dans un document PDF, vous pouvez utiliser [MovieAnnotaiton](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.movie_annotation). Une Annotation de Film contient des graphiques animés et du son à présenter sur l'écran de l'ordinateur et à travers les haut-parleurs.

Une [Annotation Sonore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.sound_annotation) doit être analogue à une annotation de texte, sauf qu'au lieu d'une note textuelle, elle contient du son enregistré à partir du microphone de l'ordinateur ou importé depuis un fichier. Lorsque l'annotation est activée, le son doit être joué. L'annotation doit se comporter comme une annotation de texte dans la plupart des cas, avec une icône différente (par défaut, un haut-parleur) pour indiquer qu'elle représente un son.

Cependant, lorsqu'il est nécessaire d'intégrer des médias à l'intérieur d'un document PDF, vous devez utiliser [RichMediaAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.rich_media_annotation).
## Ajouter une Annotation d'Écran

Le code suivant montre comment ajouter une Annotation d'Écran à un fichier PDF :

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MultimediaAnnotations::AddScreenAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"input.swf";

    // Créer une Annotation d'Écran
    auto screenAnnotation = MakeObject<ScreenAnnotation>(page, MakeObject<Rectangle>(170, 190, 470, 380), mediaFile);
    page->get_Annotations()->Add(screenAnnotation);

    document->Save(_dataDir + u"sample_swf.pdf");
}
```

## Ajouter une Annotation Sonore

Le code suivant montre comment ajouter une Annotation Sonore à un fichier PDF :

```cpp
  void MultimediaAnnotations::AddSoundAnnotation()
{

    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"file_example_WAV_1MG.wav";

    // Créer une Annotation Sonore
    auto soundAnnotation = MakeObject<SoundAnnotation>(page, new Rectangle(20, 700, 60, 740), mediaFile);
    soundAnnotation->set_Color(Color::get_Blue());
    soundAnnotation->set_Title(u"John Smith");
    soundAnnotation->set_Subject(u"Démonstration d'Annotation Sonore");
    soundAnnotation->set_Popup(MakeObject<PopupAnnotation>(document));

    page->get_Annotations()->Add(soundAnnotation);

    document->Save(_dataDir + u"sample_wav.pdf");
}
```

## Ajouter RichMediaAnnotation

Le code suivant montre comment ajouter RichMediaAnnotation à un fichier PDF :

```cpp
       void MultimediaAnnotations::AddRichMediaAnnotation()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();

    String pathToAdobeApp (u"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins");
    auto page = document->get_Pages()->Add();

    // donner un nom aux données vidéo. Ces données seront intégrées dans le document avec ce
    // nom et référencées à partir des variables flash par ce nom.
    // videoName ne doit pas contenir le chemin du fichier ; c'est plutôt une "clé" pour accéder
    // aux données à l'intérieur du document PDF

    String videoName (u"file_example_MP4_480_1_5MG.mp4");
    String posterName (u"file_example_MP4_480_1_5MG_poster.jpg");

    // nous utilisons également un habillage pour le lecteur vidéo
    String skinName (u"SkinOverAllNoFullNoCaption.swf");

    auto rma = MakeObject<RichMediaAnnotation>(page, MakeObject<Rectangle>(100, 500, 300, 600));

    // ici nous devons spécifier le flux contenant le code du lecteur vidéo
    rma->set_CustomPlayer(System::IO::File::OpenRead(pathToAdobeApp + u"Players\\" + u"Videoplayer.swf"));

    // composer la ligne de variables flash pour le lecteur. veuillez noter que différents lecteurs
    // peuvent avoir un format différent de la ligne de variables flash.
    // Référez-vous à la documentation pour votre lecteur.
    rma->set_CustomFlashVariables(u"source=" + videoName + u"&skin=" + skinName);

    // ajouter le code de l'habillage.
    rma->AddCustomData(skinName, System::IO::File::OpenRead(pathToAdobeApp + u"SkinOverAllNoFullNoCaption.swf"));
    // définir l'affiche pour la vidéo
    rma->SetPoster(System::IO::File::OpenRead(_dataDir + posterName));

    // définir le contenu vidéo
    rma->SetContent(videoName, System::IO::File::OpenRead(_dataDir + videoName));

    // définir le type de contenu (vidéo)
    rma->set_Type(RichMediaAnnotation::ContentType::Video);

    // activer le lecteur par clic
    rma->set_ActivateOn(RichMediaAnnotation::ActivationEvent::Click);

    // mettre à jour les données de l'annotation. Cette méthode doit être appelée après toutes les
    // affectations/configurations. Cette méthode initialise la structure de données de l'annotation
    // et intègre les données requises.
    rma->Update();

    // ajouter l'annotation sur la page.
    page->get_Annotations()->Add(rma);

    document->Save(_dataDir + u"RichMediaAnnotation.pdf");
}
```

### Obtenir MultimediaAnnotation

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir MultimediaAnnotation à partir du document PDF.

```cpp
void MultimediaAnnotations::GetMultimediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        Console::WriteLine(u"{0} {1}", ma->get_AnnotationType(), ma->get_Rect());
    }
}
```

### Supprimer MultimediaAnnotation

L'extrait de code suivant montre comment supprimer MultimediaAnnotation d'un fichier PDF.

```cpp
void MultimediaAnnotations::DeleteRichMediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        page->get_Annotations()->Delete(ma);
    }
    document->Save(_dataDir + u"RichMediaAnnotation_del.pdf");
}
```

## Ajouter une Annotation 3D

Aujourd'hui, les fichiers PDF peuvent contenir une variété de contenus autres que le simple texte et les graphiques, y compris des structures logiques, des éléments interactifs tels que des annotations et des champs de formulaire, des calques, des multimédias (y compris du contenu vidéo) et des objets 3D.

Ce contenu 3D peut être visualisé dans un fichier PDF à l'aide d'annotations 3D.

Cette section montre les étapes de base pour créer une annotation 3D dans un document PDF en utilisant la bibliothèque C++ de Aspose.PDF.

L'annotation 3D est ajoutée en utilisant un modèle créé au format U3D.

1. Créez un nouveau [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/)
1. Chargez les données du modèle 3D souhaité (dans notre cas "Ring.u3d") pour créer [PDF3DContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_content/)
1. Créez un objet [3dArtWork](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_artwork/) et liez-le au document et à 3DContent
1. Réglez l'objet pdf3dArtWork :

```cpp
void MultimediaAnnotation::Add3DAnnottaion()
{
    public static void Add3dAnnotation()
    {
        // Chargez le fichier PDF
        Document document = new Document();
        PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
        PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
        pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        var topMatrix = new Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
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

        document.save(_dataDir + "sample_3d.pdf");
    }
}
```

This code example showed us such a model:

![3D Annotation demo](3d_demo.png)


## Ajouter une annotation de widget

Une annotation de widget représente l'apparence des champs de formulaire dans un formulaire PDF interactif.

Depuis la version PDF 1.2, nous pouvons utiliser des annotations de widget. Ce sont des éléments de formulaire interactifs que nous pouvons ajouter au PDF pour faciliter la saisie, la soumission d'informations ou l'exécution d'une autre action avec l'utilisateur. Bien que les widgets soient un type spécial d'annotation, nous ne pouvons pas les créer directement comme annotations, car les annotations de widget sont une représentation graphique d'un champ de formulaire sur des pages spécifiques.

Chaque champ de formulaire pour chaque emplacement dans le document représente un widget d'annotation. Les données d'annotation spécifiques à l'emplacement pour le widget sont ajoutées à une page spécifique. Chaque champ de formulaire a plusieurs options. Un bouton peut être un bascule, une case à cocher ou un bouton. Le widget de sélection peut être une liste déroulante ou une boîte combinée.


Aspose.PDF pour C++ vous permet d'ajouter cette annotation en utilisant la classe [Widget Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.widget_annotation/).

Pour ajouter un bouton à la page, nous devons utiliser l'extrait de code suivant :

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;

void ExampleWidgetAnnotation::AddButton() {

    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto rect = MakeObject<Rectangle>(72, 748, 164, 768);

    auto printButton = MakeObject<ButtonField>(page, rect);
    printButton->set_AlternateName(u"Imprimer le document actuel");
    printButton->set_Color(Color::get_Black());
    printButton->set_PartialName(u"printBtn1");
    printButton->set_NormalCaption(u"Imprimer le document");

    auto border = MakeObject<Border>(printButton);
    border->set_Style(BorderStyle::Solid);
    border->set_Width(2);

    printButton->set_Border(border);
    printButton->get_Characteristics()->set_Border(System::Drawing::Color::FromArgb(255, 0, 0, 255));
    printButton->get_Characteristics()->set_Background(System::Drawing::Color::FromArgb(255, 0, 191, 255));
    auto wa = System::DynamicCast<Field>(printButton);
    document->get_Form()->Add(wa);

    document->Save(_dataDir + u"sample_widgetannot.pdf");
}
```

### Utilisation des actions de navigation dans le document

Cet exemple montre comment créer 4 boutons :

```cpp
void ExampleWidgetAnnotation::AddDocumentNavigationActions() {

    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"JSON Fundamenals.pdf");

    auto buttons = MakeArray<System::SmartPtr<ButtonField>>(4);
    auto alternateNames = MakeArray<String>({ u"Aller à la première page", u"Aller à la page précédente", u"Aller à la page suivante", u"Aller à la dernière page" });
    auto normalCaptions = MakeArray<String>({ u"Première", u"Précédente", u"Suivante", u"Dernière" });
    PredefinedAction actions[] = { PredefinedAction::FirstPage, PredefinedAction::PrevPage,
                                    PredefinedAction::NextPage, PredefinedAction::LastPage };
    auto clrBorder = System::Drawing::Color::FromArgb(255, 0, 255, 0);
    auto clrBackGround = System::Drawing::Color::Color::FromArgb(255, 0, 96, 70);

// Nous devons créer les boutons sans les attacher à la page.

    for (int i = 0; i < 4; i++) {
        buttons[i] = MakeObject<ButtonField>(document, MakeObject<Rectangle>(32 + i * 80, 28, 104 + i * 80, 68));
        buttons[i]->set_AlternateName(alternateNames[i]);
        buttons[i]->set_Color(Color::get_White());
        buttons[i]->set_NormalCaption(normalCaptions[i]);
        buttons[i]->set_OnActivated(new NamedAction(actions[i]));
        auto border = MakeObject<Border>(buttons[i]);
        border->set_Style(BorderStyle::Solid);
        border->set_Width(2);
        buttons[i]->set_Border(border);
        buttons[i]->get_Characteristics()->set_Border(clrBorder);
        buttons[i]->get_Characteristics()->set_Background(clrBackGround);
    }

// Nous devons dupliquer cet ensemble de boutons sur chaque page du document.

    for (int pageIndex = 1; pageIndex <= 4; pageIndex++)
        for (int i = 0; i < 4; i++)
            document->get_Form()->Add(buttons[i], String::Format(u"btn{0}_{1}", pageIndex,(i + 1)), pageIndex);

    document->get_Form()->idx_get(u"btn1_1")->set_ReadOnly(true);
    document->get_Form()->idx_get(u"btn1_2")->set_ReadOnly(true);

    document->get_Form()->idx_get(String::Format(u"btn{0}_3", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->get_Form()->idx_get(String::Format(u"btn{0}_4", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->Save(_dataDir + u"sample_widgetannot_2.pdf");
}
```

### Supprimer l'Annotation du Widget

```cpp
void ExampleWidgetAnnotation::DeleteWidgetAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_widgetannot.pdf");
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(MakeObject<ButtonField>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto buttonFields = annotationSelector->get_Selected();

    // supprimer les annotations
    for (auto wa : buttonFields) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_widgetannot_del.pdf");
}
```