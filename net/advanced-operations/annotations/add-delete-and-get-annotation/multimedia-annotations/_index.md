---
title: PDF Multimedia Annotations
linktitle: Multimedia Annotations
type: docs
weight: 40
url: /net/multimedia-annotation/
description: Aspose.PDF for .NET allows you to add, get, and delete the multimedia annotation from your PDF document.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Annotations in a PDF document are contained in a [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object’s Annotations collection. This collection contains all annotations for that individual page only: every page has its own Annotations collection. To add an annotation to a particular page, add it to that page’s Annotations collection using the Add method.

Use the [ScreenAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) class in the Aspose.PDF.InteractiveFeatures.Annotations namespace to include SWF files as annotations in a PDF document instead. A screen annotation specifies a region of a page upon which media clips may be played.

When you need to add an external video link in PDF document, you can use [MovieAnnotaiton](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation).
A Movie Annotation contains animated graphics and sound to be presented on the computer screen and through the speakers.

A [Sound Annotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) shall analogous to a text annotation except that instead of a text note, it contains sound recorded from the computer’s microphone or imported from a file. When the annotation is activated, the sound shall be played. The annotation shall behave like a text annotation in most ways, with a different icon (by default, a speaker) to indicate that it represents a sound.

However, when there is a requirement to embed media inside PDF document, you need to use [RichMediaAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

The following methods/properties of RichMediaAnnotation class can be used.

- Stream CustomPlayer { set; }: Allows setting player used to play video.
- string CustomFlashVariables { set; }: Allows to set variables that are passed to flash application. This line is set of “key=value” pairs which are separated with ‘&'.
- void AddCustomData(strig name, Stream data):  Add additional data for the player. For example source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}:  Event activates player; possible values are Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Set video/audio data to be playedю
- void Update():  Create a data structure of the annotation. This method should be called last
- void SetPoster(Stream): Set poster of the video i.e. picture shown when the player is not active

## Add Screen Annotation

The following code snippet shows how to add Screen Annotation to a PDF file:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.IO;
using System.Linq;


namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleMultimediaAnnotation
    {
        // The path to the documents directory.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddScreenAnnotation()
        {
            // Load the PDF file
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "input.swf");
            // Create Screen Annotation
            var screenAnnotation = new ScreenAnnotation(
                document.Pages[1],
                new Rectangle(170, 190, 470, 380),
                mediaFile);
            document.Pages[1].Annotations.Add(screenAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_swf.pdf"));
        }
    }
}
```

## Add Sound Annotation

The following code snippet shows how to add Sound Annotation to a PDF file:

```csharp
        public static void AddSoundAnnotation()
        {
            // Load the PDF file
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "file_example_WAV_1MG.wav");
            // Create Sound Annotation
            var soundAnnotation = new SoundAnnotation(
                document.Pages[1],
                new Rectangle(20, 700, 60, 740),
                mediaFile)
            {
                Color = Color.Blue,
                Title = "John Smith",
                Subject = "Sound Annotation demo",
                Popup = new PopupAnnotation(document)
            };

            document.Pages[1].Annotations.Add(soundAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_wav.pdf"));
        }
```

## Add RichMediaAnnotation

The following code snippet shows how to add RichMediaAnnotation to a PDF file:

```csharp
        public static void AddRichMediaAnnotation()
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
            var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
            Page page = doc.Pages.Add();
            //give name to video data. This data will be embedded into document with this name and referenced from flash variables by this name.
            //videoName should not contain path to the file; this is rather "key" to access data inside of the PDF document
            const string videoName = "file_example_MP4_480_1_5MG.mp4";
            const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
            //also we use skin for video player
            string skinName = "SkinOverAllNoFullNoCaption.swf";
            RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600))
            {
                //here we should specify stream containing code of the video player
                CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp,"Players","Videoplayer.swf"), FileMode.Open, FileAccess.Read),
                //compose flash variables line for player. please note that different players may have different format of the flash variables line. Refer to documentation for your player.
                CustomFlashVariables = $"source={videoName}&skin={skinName}"
            };
            //add skin code.
            rma.AddCustomData(skinName,
                new FileStream(Path.Combine(pathToAdobeApp,"SkinOverAllNoFullNoCaption.swf"), FileMode.Open, FileAccess.Read));
            //set poster for video
            rma.SetPoster(new FileStream(Path.Combine(_dataDir, posterName), FileMode.Open, FileAccess.Read));

            Stream fs = new FileStream(Path.Combine(_dataDir,videoName), FileMode.Open, FileAccess.Read);

            //set video content
            rma.SetContent(videoName, fs);

            //set type of the content (video)
            rma.Type = RichMediaAnnotation.ContentType.Video;

            //active player by click
            rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

            //update annotation data. This method should be called after all assignments/setup. This method initializes data structure of the annotation and embeds required data.
            rma.Update();

            //add annotation on the page.
            page.Annotations.Add(rma);

            doc.Save(Path.Combine(_dataDir,"RichMediaAnnotation.pdf"));
        }
```

### Get MultimediaAnnotation

Please try using the following code snippet to Get MultimediaAnnotation from PDF document.

```csharp
        public static void GetMultimediaAnnotation()
        {
            // Load the PDF file
            Document document = new Document(
                Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var mediaAnnotations = document.Pages[1].Annotations
                .Where(a => (a.AnnotationType == AnnotationType.Screen)
                || (a.AnnotationType == AnnotationType.Sound)
                || (a.AnnotationType == AnnotationType.RichMedia))
                .Cast<Annotation>();
            foreach (var ma in mediaAnnotations)
            {
                Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
            }
        }
```

### Delete MultimediaAnnotation

The following code snippet shows how to Delete MultimediaAnnotation from PDF file.

```csharp
        public static void DeletePolyAnnotation()
        {
            // Load the PDF file
            Document document = new Document(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var richMediaAnnotations = document.Pages[1].Annotations
                            .Where(a => a.AnnotationType == AnnotationType.RichMedia)
                            .Cast<RichMediaAnnotation>();

            foreach (var rma in richMediaAnnotations)
            {
                document.Pages[1].Annotations.Delete(rma);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation_del.pdf"));
        }
```

## Add Widget Annotations

Interactive forms use [Widget Annotations](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) to represent the appearance of fields and to manage user interactions.
We use these form elements that add to a PDF to make it easier to enter, submit information, or perform some other user interactions.

Widget Annotations are a graphical representation of a form field on specific pages, so we cannot create it directly as an annotation.

Each Widget Annotation will have appropriate graphics (appearance) depending on its type. After creation, certain visual aspects can be changed, such as border style and background color.
Other properties such as text color and font can be changed through the field, once attached to one.

In some cases, you may want a field to appear on more than one page, repeating the same value. In that case, fields that normally have just one widget may have multiple widgets attached: a TextField, ListBox, ComboBox, and CheckBox usually have exactly one, while the RadioGroup has multiple widgets, one for each radio button.
Someone filling out the form may use any of those widgets to update the field's value, and this is reflected in all the other widgets as well.

Each form field for each place in the document represents one Widget Annotation. The location-specific data of Widget Annotation are added to the particular page. Each form field has several variations. A button can be a radio button, a checkbox, or a push-button. A choice widget can be a list box or a combo box.

In this sample, we will learn how to add the push-buttons for navigation in the document.

### Add Button to the Document

```csharp
document = new Document();
var page = document.Pages.Add();
var rect = new Rectangle(72, 748, 164, 768);
var printButton = new ButtonField(page, rect)
{
    AlternateName = "Print current document",
    Color = Color.Black,
    PartialName = "printBtn1",
    NormalCaption = "Print Document"
};
var border = new Border(printButton)
{
    Style = BorderStyle.Solid,
    Width = 2
};
printButton.Border = border;
printButton.Characteristics.Border =
    System.Drawing.Color.FromArgb(255, 0, 0, 255);
printButton.Characteristics.Background = 
    System.Drawing.Color.FromArgb(255, 0, 191, 255);
document.Form.Add(printButton);
```

This button has border and set a background. Also we set a button name (Name), a tooltip (AlternateName), a label (NormalCaption), and a color of the label text (Color).

### Using Document-navigation actions

Exist more complex example of the Widget Annotations usage - document navigation in PDF document. This may be needed to prepare a PDF document presentation.
 
This example shows how to create 4 buttons:

```csharp
var document = new Document(@"C:\\tmp\\JSON Fundamenals.pdf");
var buttons = new ButtonField[4];
var alternateNames = new[] { "Go to first page", "Go to prev page", "Go to next page", "Go to last page" };
var normalCaptions = new[] { "First", "Prev", "Next", "Last" };
PredefinedAction[] actions = {
PredefinedAction.FirstPage,
PredefinedAction.PrevPage,
PredefinedAction.NextPage,
PredefinedAction.LastPage };
var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);
```

We should create the buttons without attaching them to the page.

```csharp
for (var i = 0; i < 4; i++)
{
    buttons[i] = new ButtonField(document,
           new Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
    {
       AlternateName = alternateNames[i],
       Color = Color.White,
       NormalCaption = normalCaptions[i],
       OnActivated = new NamedAction(actions[i])
    };
    buttons[i].Border = new Border(buttons[i])
    {
       Style = BorderStyle.Solid,
       Width = 2
    };
    buttons[i].Characteristics.Border = clrBorder;
    buttons[i].Characteristics.Background = clrBackGround;
}
```

We should duplicate this array of buttons on each page in the document.

```csharp
for (var pageIndex = 1; pageIndex <= document.Pages.Count;
                                                        pageIndex++)
    for (var i = 0; i < 4; i++)
        document.Form.Add(buttons[i],
          $"btn{pageIndex}_{i + 1}", pageIndex);

```

We call [Form.Add method](https://apireference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) with the following parameters: field, name, and the index of the pages that this field will be added to.

And to get the full result, we need disable the “First” and “Prev” buttons on the first page and the “Next” and “Last” buttons on the last page.

```csharp
document.Form["btn1_1"].ReadOnly = true;
document.Form["btn1_2"].ReadOnly = true;

document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
```

For more detailed information and possibilities of this features see also the [Working with Forms](/pdf/net/acroforms/).

In PDF documents, you can view and manage high-quality 3D content created with 3D CAD or 3D modeling software and embedded in the PDF document. Can rotate 3D elements in all directions as if you were holding them in your hands.

Why do you need a 3D display of images at all?

Over the past few years, tech has made huge breakthroughs in all areas thanks to 3D printing. 3D printing technologies can be applied to teach technological skills in construction, mechanical engineering, design as the main tool. These technologies thanks to the emergence of personal printing devices can contribute to the introduction of new forms of organization of the educational process, increase motivation, and formation of the necessary competencies of graduates
and teachers.

The main task of 3D modeling is the idea of a future object or object because, in order to release an object, you need an understanding of its design features in all detail for successive regeneration in industrial design or architecture.

## Add 3D Annotation

3D annotation is added using a model created in the U3D format.

1. Create a new [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document)
1. Load the data of the desired 3D model (in our case "Ring.u3d") to create [PDF3DContent](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent)
1. Create [3dArtWork](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) object and link it to the document and 3DContent
1. Tune pdf3dArtWork object:

    - 3DLightingScheme - (we will set  `CAD` in example)
    - 3DRenderMode - (we will set `Solid` in example)
    - Fill `ViewArray`, create at least one [3D View](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) and add it to array.

1. Set 3 basic parameters in annotation:
    - the `page` on which the annotation will be placed,
    - the `rectangle`, inside which the annotation,
    - and the `3dArtWork` object.
1. For a better presentation of the 3D object, set the Border frame
1. Set the default view (for example - TOP)
1. Add some additional parameters: name, preview poster etc.
1. Add Annotation to the [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page)
1. Save the result

### Example

Please check the following code snippet to add 3D Annotation.

```csharp
    public static void Add3dAnnotation()
    {
    // Load the PDF file
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(System.IO.Path.Combine(_dataDir,"Ring.u3d"));
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent)
    {
        LightingScheme = new PDF3DLightingScheme(LightingSchemeType.CAD),
        RenderMode = new PDF3DRenderMode(RenderModeType.Solid),
    };
    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.Pages.Add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.Border = new Border(pdf3dAnnotation);
    pdf3dAnnotation.SetDefaultViewIndex(1);
    pdf3dAnnotation.Flags = AnnotationFlags.NoZoom;    
    pdf3dAnnotation.Name = "Ring.u3d";
    //set preview image if needed
    //pdf3dAnnotation.SetImagePreview(System.IO.Path.Combine(_dataDir, "sample_3d.png"));
    document.Pages[1].Annotations.Add(pdf3dAnnotation);

    document.Save(System.IO.Path.Combine(_dataDir, "sample_3d.pdf"));
    }
```

This code example showed us such a model:

![3D Annotation demo](3d_demo.png)
