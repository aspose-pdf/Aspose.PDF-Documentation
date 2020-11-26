---
title: Add Multimedia Annotation
type: docs
weight: 120
url: /net/add-multimedia-annotation/
description: Aspose.PDF for .NET allows you to add, get, and delete the multimedia annotation from your PDF document.
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
- void AddCustomData(strig name, Stream data):  Add additional data for the player. For example source=video.mp4&autoPlay=true&scale=100ю
- ActivationEvent ActivateOn { get; set}:  Event activates player; possible values are Click, PageOpen, PageVisibleю
- void SetContent(Stream stream, string name): Set video/audio data to be playedю
- void Update():  Create a data structure of the annotation. This method should be called lastю
- void SetPoster(Stream): Set poster of the video i.e. picture shown when the player is not active

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
```        
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
    }
}
```



