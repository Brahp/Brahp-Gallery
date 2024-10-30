# init python:
#     scale = 0.5
#     currentmenu = "main_menu"
#     previousmenu = "main_menu"
#     currentGalleryPage = 1  
#     brahpgalleryCurrentPage = 1  
#     latestartCurrentPage = 1
#     featuredprojectCurrentPage = 1
#     imageCurrentIndex = 0
#     imageCurrentImage = None
    
#     brahpgalleryImageList = sorted([f for f in renpy.list_files(common=False) if f.startswith("images/gallery/") and "galleryimage" in f and f.endswith(".png")])
#     latestartImageList = sorted([f for f in renpy.list_files(common=False) if f.startswith("images/latestart/") and "galleryimage" in f and f.endswith(".png")])
#     featuredprojectImageList = sorted([f for f in renpy.list_files(common=False) if f.startswith("images/featuredproject/") and "galleryimage" in f and f.endswith(".png")])


#     imageList = brahpgalleryImageList

#     def update_image_list(new_list, gridCol, gridRow):
#         global imageList, galleryTotalPages, galleryslotsPerPage
#         imageList = new_list
#         galleryslotsPerPage = gridCol * gridRow
#         galleryTotalPages = (len(imageList) + galleryslotsPerPage - 1) // galleryslotsPerPage

#     def change_image(delta):
#         global imageCurrentIndex, imageCurrentImage, brahpgalleryCurrentPage
#         imageCurrentIndex = (imageCurrentIndex + delta) % len(imageList)
#         imageCurrentImage = imageList[imageCurrentIndex]


#     def showmenu(menu_name):
#         global currentmenu, previousmenu
#         previousmenu = currentmenu
#         currentmenu = menu_name
#         renpy.show_screen(menu_name)


#     config.renpy.ShowMenu = showmenu



# screen navigation():

#     vbox:
#         style_prefix "navigation"

#         xpos gui.navigation_xpos
#         yalign 0.5

#         spacing gui.navigation_spacing

#         if main_menu:
#             textbutton _("Brahps Gallery") action Function(showmenu, "brahpgallery")

#             textbutton _("Home") action Function(showmenu, "home")

#         # if main_menu:

#             # textbutton _("Start") action Start()

#         # else:

#         #     textbutton _("History") action ShowMenu("history")

#         #     textbutton _("Save") action ShowMenu("save")

#         # textbutton _("Load") action ShowMenu("load")

#         # textbutton _("Preferences") action ShowMenu("preferences")


#         if _in_replay:

#             textbutton _("End Replay") action EndReplay(confirm=True)

#         elif not main_menu:

#             textbutton _("Main Menu") action MainMenu()

#         textbutton _("About") action ShowMenu("about")
 

#         # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

#         #     ## Help isn't necessary or relevant to mobile devices.
#         #     textbutton _("Help") action ShowMenu("help")

#         if renpy.variant("pc"):

#             ## The quit button is banned on iOS and unnecessary on Android and
#             ## Web.
#             textbutton _("Quit") action Quit(confirm=not main_menu)


# style navigation_button is gui_button
# style navigation_button_text is gui_button_text

# style navigation_button:
#     size_group "navigation"
#     properties gui.button_properties("navigation_button")

# style navigation_button_text:
#     properties gui.text_properties("navigation_button")









# screen brahpgallery():
#     tag menu
#     use game_menu(_("Brahp Gallery")):
#         $ update_image_list(brahpgalleryImageList, 3, 2)
#         use gallery_slots(imageList, 3, 2)





# label gallerylogic:


#     screen gallery_slots(imageList, gridCol, gridRow):
#         tag menu

#         $ galleryslotsPerPage = gridCol * gridRow
#         $ galleryTotalPages = (len(imageList) + galleryslotsPerPage - 1) // galleryslotsPerPage

#         fixed:
#             order_reverse True

#             grid gridCol gridRow:
#                 style_prefix "slot"
#                 xalign 0.5
#                 yalign 0.5
#                 spacing gui.slot_spacing

#                 for i in range(galleryslotsPerPage):
#                     $ slot = (brahpgalleryCurrentPage - 1) * galleryslotsPerPage + i
#                     if slot < len(imageList):
#                         $ imageName = imageList[slot]

#                         button:
#                             action [
#                                 SetVariable("imageCurrentImage", imageName),
#                                 SetVariable("imageCurrentIndex", slot),
#                                 Function(showmenu, "show_full_image")
#                             ]
#                             has vbox

#                             frame:
#                                 xsize gui.slot_button_width - 20
#                                 ysize gui.slot_button_height

#                                 add Transform(
#                                     Image(imageName),
#                                     size=(gui.slot_button_width - 200, gui.slot_button_height - 20), 
#                                     xalign=0.5,
#                                     yalign=0.5
#                                 )

#             # Pagination buttons for brahpgallery
#             vbox:
#                 style_prefix "page"
#                 xalign 0.5
#                 yalign 1.0

#                 hbox:
#                     xalign 0.5
#                     spacing gui.page_spacing

#                     textbutton _("<") action SetVariable("brahpgalleryCurrentPage", max(brahpgalleryCurrentPage - 1, 1))
#                     for page in range(1, galleryTotalPages + 1):
#                         textbutton str(page) action SetVariable("brahpgalleryCurrentPage", page)
#                     textbutton _(">") action SetVariable("brahpgalleryCurrentPage", min(brahpgalleryCurrentPage + 1, galleryTotalPages))




#     screen PageGallerySlot(galleryCurrentPage, imageList, gridCol, gridRow):
#         tag menu

#         $ galleryslotsPerPage = gridCol * gridRow
#         $ galleryTotalPages = (len(imageList) + galleryslotsPerPage - 1) // galleryslotsPerPage

#         grid gridCol gridRow:
#             style_prefix "slot"
#             xalign 0.5
#             yalign 0.5
#             spacing gui.slot_spacing
            
#             for i in range(galleryslotsPerPage):
#                 $ slot = (galleryCurrentPage - 1) * galleryslotsPerPage + i
#                 if slot < len(imageList):
#                     $ imageName = imageList[slot]
#                     button:
#                         action [
#                             SetVariable("imageCurrentImage", imageName),
#                             SetVariable("imageCurrentIndex", slot),
#                             Function(showmenu, "show_full_image")
#                         ]
#                         has vbox
#                         frame:
#                             xsize gui.slot_button_width - 20
#                             ysize gui.slot_button_height
#                             add Transform(
#                                 Image(imageName),
#                                 size=(gui.slot_button_width - 200, gui.slot_button_height - 20),
#                                 xalign=0.5,
#                                 yalign=0.5
#                             )


# screen show_full_image():
#     tag menu

#     vbox:
#         xalign 0.5
#         yalign 0.5

      
#         $ width, height = renpy.image_size(imageCurrentImage)

#         frame:
#             xsize 1920
#             ysize 1050
#             xalign 0.5
#             yalign 0.5
#             padding (0, 20)  

#             if imageCurrentImage:
#                 add Transform(
#                     Image(imageCurrentImage), size=(width * scale, height * scale)
#                 ) xalign 0.5 yalign 0.5

       
#             hbox:
#                 xalign 0.5
#                 yalign 1.0
#                 spacing 1000 

            
#                 textbutton "<" action Function(change_image, -1): 
#                     xalign 0  

            
#                 textbutton ">" action Function(change_image, 1):
#                     xalign 1  


#     textbutton _("Return"): 
#             style "return_button"
#             action [SetVariable("imageCurrentImage", None), Function(showmenu, previousmenu)]



#     key "K_LEFT" action Function(change_image, -1)
#     key "K_RIGHT" action Function(change_image, 1)





# label homescreen:

#     screen home():
#         tag menu

#         use game_menu(_("Home"), scroll="viewport"):
#             style_prefix "about"

#             vbox:
#                 label "Latest Art"
#                 use latest_art()

#                 label "Featured Projects"
#                 use featured_project()


#     screen latest_art():
#         tag menu
#         use PageGallerySlot(latestartCurrentPage, latestartImageList, 3, 1)

    

#     screen featured_project():
#         use PageGallerySlot(featuredprojectCurrentPage, featuredprojectImageList, 3, 1)


































init python:
    scale = 0.5
    currentmenu = "main_menu"
    previousmenu = "main_menu"
    currentGalleryPage = 1  
    brahpgalleryPage = 1  
    latestartPage = 1
    featuredprojectPage = 1
    imageCurrentIndex = 0
    imageCurrentImage = None
    
    # Image lists
    brahpgalleryImageList = sorted([f for f in renpy.list_files(common=False) if f.startswith("images/gallery/") and "galleryimage" in f and f.endswith(".png")])
    latestartImageList = sorted([f for f in renpy.list_files(common=False) if f.startswith("images/latestart/") and "galleryimage" in f and f.endswith(".png")])
    featuredprojectImageList = sorted([f for f in renpy.list_files(common=False) if f.startswith("images/featuredproject/") and "galleryimage" in f and f.endswith(".png")])

    # Default image list for general access
    imageList = brahpgalleryImageList

    def update_image_list(new_list, gridCol, gridRow):
        global imageList, galleryTotalPages, galleryslotsPerPage
        imageList = new_list
        galleryslotsPerPage = gridCol * gridRow
        galleryTotalPages = (len(imageList) + galleryslotsPerPage - 1) // galleryslotsPerPage

    def change_image(delta):
        global imageCurrentIndex, imageCurrentImage, currentGalleryPage
        imageCurrentIndex = (imageCurrentIndex + delta) % len(imageList)
        imageCurrentImage = imageList[imageCurrentIndex]
        
        # Update current gallery page based on image index
        currentGalleryPage = (imageCurrentIndex // galleryslotsPerPage) + 1

    def showmenu(menu_name):
        global currentmenu, previousmenu
        previousmenu = currentmenu
        currentmenu = menu_name
        renpy.show_screen(menu_name)

    config.renpy.ShowMenu = showmenu


screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Brahps Gallery") action [SetVariable("currentGalleryPage", brahpgalleryPage), Function(showmenu, "brahpgallery")]:
                selected (currentmenu == "brahpgallery")
            textbutton _("Home") action Function(showmenu, "home"):
                selected (currentmenu == "home")

        textbutton _("About") action Function(showmenu, "about"):
            selected (currentmenu == "about")
        
        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu)


screen brahpgallery():
    tag menu
    use game_menu(_("Brahp Gallery")):
        $ update_image_list(brahpgalleryImageList, 3, 2)
        use gallery_slots(imageList, 3, 2)


screen gallery_slots(imageList, gridCol, gridRow):
    tag menu
    $ galleryslotsPerPage = gridCol * gridRow
    $ galleryTotalPages = (len(imageList) + galleryslotsPerPage - 1) // galleryslotsPerPage

    fixed:
        grid gridCol gridRow:
            style_prefix "slot"
            xalign 0.5
            yalign 0.5
            spacing gui.slot_spacing

            for i in range(galleryslotsPerPage):
                $ slot = (currentGalleryPage - 1) * galleryslotsPerPage + i
                if slot < len(imageList):
                    $ imageName = imageList[slot]
                    button:
                        action [
                            SetVariable("imageCurrentImage", imageName),
                            SetVariable("imageCurrentIndex", slot),
                            Function(showmenu, "show_full_image")
                        ]
                        has vbox

                        frame:
                            xsize gui.slot_button_width - 20
                            ysize gui.slot_button_height
                            add Transform(Image(imageName), size=(gui.slot_button_width - 200, gui.slot_button_height - 20), xalign=0.5, yalign=0.5)

        # Pagination buttons
        vbox:
            xalign 0.5
            yalign 1.0
            hbox:
                xalign 0.5
                spacing gui.page_spacing
                textbutton _("<") action SetVariable("currentGalleryPage", max(currentGalleryPage - 1, 1))
                for page in range(1, galleryTotalPages + 1):
                    textbutton str(page) action SetVariable("currentGalleryPage", page)
                textbutton _(">") action SetVariable("currentGalleryPage", min(currentGalleryPage + 1, galleryTotalPages))




screen PageGallerySlot(galleryCurrentPage, imageList, gridCol, gridRow):
    tag menu

    $ galleryslotsPerPage = gridCol * gridRow
    $ galleryTotalPages = (len(imageList) + galleryslotsPerPage - 1) // galleryslotsPerPage

    grid gridCol gridRow:
        style_prefix "slot"
        xalign 0.5
        yalign 0.5
        spacing gui.slot_spacing
        
        for i in range(galleryslotsPerPage):
            $ slot = (galleryCurrentPage - 1) * galleryslotsPerPage + i
            if slot < len(imageList):
                $ imageName = imageList[slot]
                button:
                    action [
                        SetVariable("imageCurrentImage", imageName),
                        SetVariable("imageCurrentIndex", slot),
                        Function(showmenu, "show_full_image")
                    ]
                    has vbox
                    frame:
                        xsize gui.slot_button_width - 20
                        ysize gui.slot_button_height
                        add Transform(
                            Image(imageName),
                            size=(gui.slot_button_width - 200, gui.slot_button_height - 20),
                            xalign=0.5,
                            yalign=0.5
                        )


screen show_full_image():
    tag menu

    vbox:
        xalign 0.5
        yalign 0.5

      
        $ width, height = renpy.image_size(imageCurrentImage)

        frame:
            xsize 1920
            ysize 1050
            xalign 0.5
            yalign 0.5
            padding (0, 20)  

            if imageCurrentImage:
                add Transform(
                    Image(imageCurrentImage), size=(width * scale, height * scale)
                ) xalign 0.5 yalign 0.5

       
            hbox:
                xalign 0.5
                yalign 1.0
                spacing 1000 

            
                textbutton "<" action Function(change_image, -1): 
                    xalign 0  

            
                textbutton ">" action Function(change_image, 1):
                    xalign 1  


    textbutton _("Return"): 
            style "return_button"
            action [SetVariable("imageCurrentImage", None), Function(showmenu, previousmenu)]



    key "K_LEFT" action Function(change_image, -1)
    key "K_RIGHT" action Function(change_image, 1)





label homescreen:

    screen home():
        tag menu

        use game_menu(_("Home"), scroll="viewport"):
            style_prefix "about"

            vbox:
                label "Latest Art"
                use latest_art()

                label "Featured Projects"
                use featured_project()


    screen latest_art():
        tag menu
        use PageGallerySlot(latestartPage, latestartImageList, 3, 1)

    

    screen featured_project():
        use PageGallerySlot(featuredprojectPage, featuredprojectImageList, 3, 1)