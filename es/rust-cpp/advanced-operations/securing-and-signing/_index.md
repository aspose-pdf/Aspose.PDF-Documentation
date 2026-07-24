---
title: Asegurar y firmar PDF en Rust
linktitle: Asegurar y firmar PDF
type: docs
weight: 50
url: /es/rust-cpp/securing-and-signing/
description: Esta sección describe las características de usar una firma y asegurar su documento PDF usando Rust
lastmod: "2026-07-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Esta sección ofrece una guía completa para trabajar con documentos PDF asegurados usando Aspose.PDF para Rust a través de C++. Explica cómo proteger archivos PDF con contraseñas, gestionar permisos de acceso y abrir o desbloquear de forma segura documentos cifrados en Rust.

El artículo repasa tareas comunes relacionadas con la seguridad en PDF, incluyendo el cifrado de PDFs con algoritmos criptográficos modernos, el descifrado de archivos protegidos con contraseña y el control del acceso de usuarios mediante banderas de permiso. También aprenderá cómo inspeccionar la configuración de permisos existente y abrir documentos asegurados usando las credenciales del propietario para su posterior procesamiento.

Aprenderá cómo crear documentos PDF, aplicar protección criptográfica moderna utilizando cifrado basado en AES y controlar las capacidades de los usuarios, como imprimir, editar contenido y rellenar formularios. El artículo también muestra cómo abrir PDFs protegidos con contraseña usando las credenciales del propietario y descifrarlos para generar documentos sin restricciones adecuados para su posterior procesamiento.

- [Cifrar un archivo PDF](/pdf/es/rust-cpp/encrypt-pdf/)
- [Descifrar archivo PDF](/pdf/es/rust-cpp/decrypt-pdf/)
- [Obtener permisos](/pdf/es/rust-cpp/get-permissions/)
- [Establecer permisos](/pdf/es/rust-cpp/set_permissions/)
- [Abrir un PDF protegido con contraseña](/pdf/es/rust-cpp/open-password-protected-pdf/)

Para trabajar con Establecer permisos y Obtener permisos, consulte la tabla de referencia de permisos de PDF, que enumera los indicadores de permiso disponibles que pueden aplicarse a un documento PDF para controlar cómo los usuarios finales interactúan con él.

## Referencia de permisos de PDF

| **Permission** | **Description** |
| :- | :- |
| Permissions::PRINT_DOCUMENT | Permitir impresión |
| Permissions::MODIFY_CONTENT | Permitir modificar contenido (excepto formularios/anotaciones) |
| Permissions::EXTRACT_CONTENT | Permitir copiar/extraer texto y gráficos |
| Permissions::MODIFY_TEXT_ANNOTATIONS | Permitir agregar/modificar anotaciones de texto |
| Permissions::FILL_FORM | Permitir rellenar formularios interactivos |
| Permissions::EXTRACT_CONTENT_WITH_DISABILITIES | Permitir la extracción de contenido para accesibilidad |
| Permissions::ASSEMBLE_DOCUMENT | Permitir insertar/rotar/eliminar páginas o cambiar la estructura |
| Permissions::PRINTING_QUALITY | Permitir impresión de alta calidad / fiel |
