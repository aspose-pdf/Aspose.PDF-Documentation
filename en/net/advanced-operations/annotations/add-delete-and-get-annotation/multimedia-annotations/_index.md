---
title: PDF Multimedia Annotation using C#
linktitle: Multimedia Annotation
type: docs
weight: 40
url: /net/multimedia-annotation/
description: Aspose.PDF for .NET allows you to add, get, and delete the multimedia annotation from your PDF document.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Multimedia Annotation using C#",
    "alternativeHeadline": "Enable Multimedia Annotations in PDF with C#",
    "abstract": "Aspose.PDF for .NET introduces advanced multimedia annotation capabilities, enabling users to seamlessly add, retrieve, and delete various multimedia types in PDF documents. This feature supports screen, sound, and rich media annotations, enhancing document interactivity and allowing for the integration of external video content, audio notes, and embedded media, making PDF documents more dynamic and engaging",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF multimedia annotation, Aspose.PDF, C# PDF features, screen annotation, sound annotation, rich media annotation, widget annotations, 3D annotation, document navigation, multimedia file embedding",
    "wordcount": "2247",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/multimedia-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/multimedia-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

Annotations in a PDF document are contained in a [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) object's Annotations collection. This collection contains all annotations for that individual page only: every page has its own Annotations collection. To add an annotation to a particular page, add it to that page's Annotations collection using the Add method.

Use the [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) class in the Aspose.PDF.InteractiveFeatures.Annotations namespace to include SWF files as annotations in a PDF document instead. A screen annotation specifies a region of a page upon which media clips may be played.

When you need to add an external video link in PDF document, you can use [MovieAnnotaiton](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation).
A Movie Annotation contains animated graphics and sound to be presented on the computer screen and through the speakers.

A [Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) shall analogous to a text annotation except that instead of a text note, it contains sound recorded from the computer's microphone or imported from a file. When the annotation is activated, the sound shall be played. The annotation shall behave like a text annotation in most ways, with a different icon (by default, a speaker) to indicate that it represents a sound.

However, when there is a requirement to embed media inside PDF document, you need to use [RichMediaAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

The following methods/properties of RichMediaAnnotation class can be used.

- Stream CustomPlayer { set; }: Allows setting player used to play video.
- string CustomFlashVariables { set; }: Allows to set variables that are passed to flash application. This line is set of “key=value” pairs which are separated with ‘&'.
- void AddCustomData(strig name, Stream data):  Add additional data for the player. For example source=video.mp4&autoPlay=true&scale=100.
- ActivationEvent ActivateOn { get; set}:  Event activates player; possible values are Click, PageOpen, PageVisible.
- void SetContent(Stream stream, string name): Set video/audio data to be played.
- void Update():  Create a data structure of the annotation. This method should be called last.
- void SetPoster(Stream): Set poster of the video i.e. picture shown when the player is not active.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Add Screen Annotation

The following code snippet shows how to add Screen Annotation to a PDF file:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddScreenAnnotationWithMedia()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open the document
    using (cument = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
	{
		// Path to the media file (SWF)
		var mediaFile = dataDir + "input.swf";

		// Create Screen Annotation
		var screenAnnotation = new Aspose.Pdf.Annotations.ScreenAnnotation(
			document.Pages[1],
			new Aspose.Pdf.Rectangle(170, 190, 470, 380),
			mediaFile);

		// Add the annotation to the page
		document.Pages[1].Annotations.Add(screenAnnotation);

		// Save the updated document
		document.Save(dataDir + "sample_swf_out.pdf");
	}
}
```

## Add Sound Annotation

The following code snippet shows how to add Sound Annotation to a PDF file:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddSoundAnnotation()
{
    // Open the document
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
	{
		var mediaFile = dataDir + "file_example_WAV_1MG.wav";

		// Create Sound Annotation
		var soundAnnotation = new Aspose.Pdf.Annotations.SoundAnnotation(
			document.Pages[1],
			new Aspose.Pdf.Rectangle(20, 700, 60, 740),
			mediaFile)
		{
			Color = Aspose.Pdf.Color.Blue,
			Title = "John Smith",
			Subject = "Sound Annotation demo",
			Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(20, 700, 60, 740))
		};

		document.Pages[1].Annotations.Add(soundAnnotation);

		// Save the document with the new annotation
		document.Save(dataDir + "sample_wav_out.pdf");
	}
}
```

## Add RichMediaAnnotation

The following code snippet shows how to add RichMediaAnnotation to a PDF file:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddRichMediaAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create a new document
    using (var document = new Aspose.Pdf.Document())
	{
		var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
		Page page = document.Pages.Add();

		// Define video and poster names
		const string videoName = "file_example_MP4_480_1_5MG.mp4";
		const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
		string skinName = "SkinOverAllNoFullNoCaption.swf";

		// Create RichMediaAnnotation
		var rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600));

		// Specify the stream containing the video player code
		rma.CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp, "Players", "Videoplayer.swf"), FileMode.Open, FileAccess.Read);

		// Compose flash variables line for the player
		rma.CustomFlashVariables = $"source={videoName}&skin={skinName}";

		// Add skin code
		rma.AddCustomData(skinName, new FileStream(Path.Combine(pathToAdobeApp, skinName), FileMode.Open, FileAccess.Read));

		// Set poster for the video
		rma.SetPoster(new FileStream(Path.Combine(dataDir, posterName), FileMode.Open, FileAccess.Read));

		// Set video content
		using (Stream fs = new FileStream(Path.Combine(dataDir, videoName), FileMode.Open, FileAccess.Read))
		{
			rma.SetContent(videoName, fs);
		}

		// Set type of the content (video)
		rma.Type = RichMediaAnnotation.ContentType.Video;

		// Activate player by click
		rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

		// Update annotation data
		rma.Update();

		// Add annotation to the page
		page.Annotations.Add(rma);

		// Save the document with the new annotation
		document.Save(dataDir + "RichMediaAnnotation_out.pdf");
	}
}
```

### Get MultimediaAnnotation

Please try using the following code snippet to Get MultimediaAnnotation from PDF document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetMultimediaAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
	{
		// Get multimedia annotations (Screen, Sound, RichMedia)
		var mediaAnnotations = document.Pages[1].Annotations
			.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Screen
						|| a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Sound
						|| a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
			.Cast<Aspose.Pdf.Annotations.Annotation>();

		// Iterate through the annotations and print their details
		foreach (var ma in mediaAnnotations)
		{
			Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
		}
	}
}
```

### Delete MultimediaAnnotation

The following code snippet shows how to Delete MultimediaAnnotation from PDF file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void DeletePolyAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
    {
        // Get RichMedia annotations
        var richMediaAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
            .Cast<Aspose.Pdf.Annotations.RichMediaAnnotation>();

        // Delete each RichMedia annotation
        foreach (var rma in richMediaAnnotations)
        {
            document.Pages[1].Annotations.Delete(rma);
        }

        // Save the document after deleting annotations
        document.Save(dataDir + "RichMediaAnnotation_del_out.pdf");
    }
}
```

## Add Widget Annotations

Interactive forms use [Widget Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) to represent the appearance of fields and to manage user interactions.
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
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddPrintButton()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create a new document
    using (var document = new Aspose.Pdf.Document())
	{
		// Add a new page
		var page = document.Pages.Add();

		// Define the rectangle for the button
		var rect = new Aspose.Pdf.Rectangle(72, 748, 164, 768);

		// Create a button field
		var printButton = new Aspose.Pdf.Forms.ButtonField(page, rect)
		{
			AlternateName = "Print current document",
			Color = Aspose.Pdf.Color.Black,
			PartialName = "printBtn1",
			NormalCaption = "Print Document"
		};

		// Set the border style for the button
		var border = new Aspose.Pdf.Annotations.Border(printButton)
		{
			Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
			Width = 2
		};
		printButton.Border = border;

		// Set the border and background color characteristics
		printButton.Characteristics.Border = System.Drawing.Color.FromArgb(255, 0, 0, 255);
		printButton.Characteristics.Background = System.Drawing.Color.FromArgb(255, 0, 191, 255);

		// Add the button to the form
		document.Form.Add(printButton);

		// Save the document
		document.Save(dataDir + "PrintButton_out.pdf");
	}
}
```

This button has border and set a background. Also we set a button name (Name), a tooltip (AlternateName), a label (NormalCaption), and a color of the label text (Color).

### Using Document-navigation actions

Exist more complex example of the Widget Annotations usage - document navigation in PDF document. This may be needed to prepare a PDF document presentation.

This example shows how to create 4 buttons:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AddNavigationButtons()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "JSON Fundamenals.pdf"))
	{
		// Create an array of button fields
		var buttons = new Aspose.Pdf.Forms.ButtonField[4];

		// Define alternate names and normal captions for the buttons
		var alternateNames = new[] { "Go to first page", "Go to prev page", "Go to next page", "Go to last page" };
		var normalCaptions = new[] { "First", "Prev", "Next", "Last" };

		// Define predefined actions for the buttons
		PredefinedAction[] actions = {
			PredefinedAction.FirstPage,
			PredefinedAction.PrevPage,
			PredefinedAction.NextPage,
			PredefinedAction.LastPage
		};

		// Define border and background colors
		var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
		var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);



		// We should create the buttons without attaching them to the page.

		for (var i = 0; i < 4; i++)
		{
			buttons[i] = new Aspose.Pdf.Forms.ButtonField(document, new Aspose.Pdf.Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
			{
				AlternateName = alternateNames[i],
				Color = Aspose.Pdf.Color.White,
				NormalCaption = normalCaptions[i],
				OnActivated = new Aspose.Pdf.Annotations.NamedAction(actions[i])
			};

			// Set the border style for the button
			buttons[i].Border = new Aspose.Pdf.Annotations.Border(buttons[i])
			{
				Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
				Width = 2
			};

			// Set the border and background color characteristics
			buttons[i].Characteristics.Border = clrBorder;
			buttons[i].Characteristics.Background = clrBackGround;
		}

		// Duplicate the array of buttons on each page in the document
		for (var pageIndex = 1; pageIndex <= document.Pages.Count; pageIndex++)
		{
			for (var i = 0; i < 4; i++)
			{
				document.Form.Add(buttons[i], $"btn{pageIndex}_{i + 1}", pageIndex);
			}
		}

		// Save the document
		document.Save(dataDir + "NavigationButtons_out.pdf");


		// We call Form.Add method with the following parameters: field, name, and the index of the pages that this field will be added to.
		// And to get the full result, we need disable the “First” and “Prev” buttons on the first page and the “Next” and “Last” buttons on the last page.

		document.Form["btn1_1"].ReadOnly = true;
		document.Form["btn1_2"].ReadOnly = true;

		document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
		document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
	}
}
```

For more detailed information and possibilities of this features see also the [Working with Forms](/pdf/net/acroforms/).

In PDF documents, you can view and manage high-quality 3D content created with 3D CAD or 3D modeling software and embedded in the PDF document. Can rotate 3D elements in all directions as if you were holding them in your hands.

Why do you need a 3D display of images at all?

Over the past few years, tech has made huge breakthroughs in all areas thanks to 3D printing. 3D printing technologies can be applied to teach technological skills in construction, mechanical engineering, design as the main tool. These technologies thanks to the emergence of personal printing devices can contribute to the introduction of new forms of organization of the educational process, increase motivation, and formation of the necessary competencies of graduates
and teachers.

The main task of 3D modeling is the idea of a future object or object because, in order to release an object, you need an understanding of its design features in all detail for successive regeneration in industrial design or architecture.

## Add 3D Annotation

3D annotation is added using a model created in the U3D format.

1. Create a new [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Load the data of the desired 3D model (in our case "Ring.u3d") to create [PDF3DContent](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent).
1. Create [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) object and link it to the document and 3DContent.
1. Tune pdf3dArtWork object:

    - 3DLightingScheme - (we will set  `CAD` in example)
    - 3DRenderMode - (we will set `Solid` in example)
    - Fill `ViewArray`, create at least one [3D View](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) and add it to array.

1. Set 3 basic parameters in annotation:
    - the `page` on which the annotation will be placed.
    - the `rectangle`, inside which the annotation.
    - and the `3dArtWork` object.
1. For a better presentation of the 3D object, set the Border frame.
1. Set the default view (for example - TOP).
1. Add some additional parameters: name, preview poster etc.
1. Add Annotation to the [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
1. Save the result.

### Example

Please check the following code snippet to add 3D Annotation.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void Add3dAnnotation()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create a new PDF document
    using (var document = new Aspose.Pdf.Document())
	{
		// Load 3D content
		var pdf3DContent = new Aspose.Pdf.Annotations.PDF3DContent(dataDir + "Ring.u3d");

		// Create 3D artwork
		var pdf3dArtWork = new Aspose.Pdf.Annotations.PDF3DArtwork(document, pdf3DContent)
		{
			LightingScheme = new Aspose.Pdf.Annotations.PDF3DLightingScheme(Aspose.Pdf.Annotations.LightingSchemeType.CAD),
			RenderMode = new Aspose.Pdf.Annotations.PDF3DRenderMode(Aspose.Pdf.Annotations.RenderModeType.Solid),
		};

		// Define matrices for different views
		var topMatrix = new Aspose.Pdf.Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
		var frontMatrix = new Aspose.Pdf.Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);

		// Add views to the 3D artwork
		pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, topMatrix, 0.188563, "Top")); //1
		pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

		// Add a new page to the document
		var page = document.Pages.Add();

		// Create a 3D annotation
		var pdf3dAnnotation = new Aspose.Pdf.Annotations.PDF3DAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 700), pdf3dArtWork);
		pdf3dAnnotation.Border = new Aspose.Pdf.Annotations.Border(pdf3dAnnotation);
		pdf3dAnnotation.SetDefaultViewIndex(1);
		pdf3dAnnotation.Flags = Aspose.Pdf.Annotations.AnnotationFlags.NoZoom;
		pdf3dAnnotation.Name = "Ring.u3d";

		// Set preview image if needed
		// pdf3dAnnotation.SetImagePreview(dataDir + "sample_3d.png");

		// Add the 3D annotation to the page
		document.Pages[1].Annotations.Add(pdf3dAnnotation);

		// Save the document
		document.Save(dataDir + "sample_3d_out.pdf");
	}
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
