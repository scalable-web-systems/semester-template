# Semester-template Contributing Guide 

This document highlights the various contributing requirements for the automated wiki. This would allow the various automations we have setup to integrate your tutorial into the system. These requirements are built into test cases in a github action which will run when you submit a pull request with your tutorial, to be able to pass all those tests, all the requirements must be satisfied. This is to ensure consistency in our tutorials and allow for quality tutorials. 

## Overall Architecture 

The way the system works is that it treats each tutorial in a markdown file as an individual component that lives and works on its own. This allows markdown files to be pulled and built into a site. 


## Markdown File Requirements

### Comment to Declare Topic 

Each tutorial must have a comment on the first line of the tutorial (before the heading). The comment should contain a number corresponding to the topics given below:

0 - Kubernetes
<br>
1 - Docker

For Example:

```
<!-- 0 -->

```

The comment with the number would tell the system which topic to place the tutorial into. 


### Images

To ensure images are stored reliably and consistently we have decided to store all images related to the tutorial in this repository: 

[Github Images Repository](https://github.com/scalable-web-systems/images)

**Steps to add your image:**

Step 1:

Clone the images repository:

```
git clone https://github.com/scalable-web-systems/images.git
```

Make a new branch with the name of branch being your github username. 

Step 2:

Add your image to the folder that corresponds to the semester, at the time of writing this guide and for this example the folder is spring-22. 

Use the following format for the image name:

```
github_username_file_description

Example:

abhinavtripathy_kubernetes_demo

```

![](https://github.com/scalable-web-systems/images/blob/main/admin/adding_images_1.png?raw=true)


Step 3:

Navigate to the images repository: 

[Github Images Repository](https://github.com/scalable-web-systems/images)

and navigate to your file shown as below:

![](https://github.com/scalable-web-systems/images/blob/main/admin/adding_images_2.png?raw=true)


Step 4:

Right click on the image and click on "copy image URL". The URL that will be copied will be the URL of the image file which can be embedded in a markdown file as such:

```
![](IMAGE_URL_LINK)

```

Picture of what happens when you right click on the image:

![](https://github.com/scalable-web-systems/images/blob/main/admin/adding_images_3.png?raw=true)

### Author Section

There must be an author section that should be right after the heading(if there is a picture right after the heading, then perhaps after that) where you mention author name and if the author wants they can include their social links.

Example:

This is how your markdown file might look like

```
### Author

Abhinav Tripathy ![Linkedin](linkedin.com/in/abhinavtripathy)

```

### Acknowledgements Section

The second last section of the tutorial must be an acknowledgements section (named exatly "Acknowledgements") where you can add links to various resources you may have used for the tutorial. Remember, as part of the scientific community, it is very important to give everyone their credit, so please don't forget to give acknowledgements!

Example:

```
## Acknowledgements

- [About kubernetes](Link 1)
- [About docker] (Link 2)
```


### Feedback Section 

The last section of the tutorial must be a feedback section(named exactly "Feedback"). You can copy paste the following for reference:

```
## Feedback

If you have any feedback or comments or want to improve something, please open an issue on github [here](https://github.com/scalable-web-systems/feedback/issues/new/choose)

```

## Submitting Your Tutorial 

To submit your tutorial to this repository, create a new branch with with it's name being your github username and then submit a pull request. You will be able to merge the pull request once all the test cases have passed. The name of the markdown file you submit must be related to your topic.


Thank you for looking to contribute to our wiki! Happy Writing!