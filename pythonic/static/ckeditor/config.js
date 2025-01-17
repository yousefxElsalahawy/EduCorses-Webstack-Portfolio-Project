/**
 * @license Copyright (c) 2003-2024, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
    // تعريف شريط الأدوات مع وضع YouTube في الأعلى
    config.toolbar = [
        { name: 'youtube-special', items: ['Youtube'] },
        { name: 'divider', items: ['-'] },  // فاصل
        { name: 'document', items: [ 'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates' ] },
        '/',  // سطر جديد
        { name: 'basicstyles', items: [ 'Bold', 'Italic', 'Strike', '-', 'RemoveFormat' ] },
        { name: 'paragraph', items: [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote' ] },
        { name: 'links', items: [ 'Link', 'Unlink' ] },
        { name: 'insert', items: [ 'Image', 'Table', 'CodeSnippet' ] }
    ];

    // إضافة الإضافات
    config.extraPlugins = 'youtube,codesnippet';

    // تخصيص CSS لزر YouTube
    CKEDITOR.addCss(`
        /* تنسيق زر YouTube */
        .cke_button__youtube {
            background: #ff0000 !important;
            padding: 10px 20px !important;
            border-radius: 5px !important;
            margin: 10px !important;
            display: flex !important;
            align-items: center !important;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2) !important;
        }

        /* تكبير وتلوين الأيقونة */
        .cke_button__youtube_icon {
            transform: scale(2.5) !important;
            filter: brightness(0) invert(1) !important;
            margin-right: 10px !important;
        }

        /* تنسيق النص */
        .cke_button__youtube .cke_button_label {
            display: inline !important;
            color: white !important;
            font-size: 16px !important;
            font-weight: bold !important;
            margin-left: 10px !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3) !important;
        }

        /* تأثير التحويم */
        .cke_button__youtube:hover {
            background: #cc0000 !important;
            transform: translateY(-2px) !important;
            transition: all 0.3s ease !important;
        }

        /* تنسيق شريط أدوات YouTube */
        .cke_toolbar_youtube-special {
            background: #f8f9fa !important;
            padding: 5px !important;
            margin-bottom: 5px !important;
            border-bottom: 2px solid #e9ecef !important;
        }
    `);

    // تعيين النص للزر
    config.on = {
        instanceReady: function(evt) {
            var editor = evt.editor;
            var youtubeButton = editor.ui.get('Youtube');
            if (youtubeButton) {
                youtubeButton.label = 'Add Lesson From Youtube';
            }
        }
    };

    // إعدادات YouTube
    config.youtube_responsive = true;
    config.youtube_controls = true;
    config.youtube_privacy = false;
    config.youtube_width = '640';
    config.youtube_height = '480';

    // إظهار النص دائماً
    config.labelShow = true;
};