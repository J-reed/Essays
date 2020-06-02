


var language_set = "English";
var blog_directory = "/Essays/blogs/English/";


function getBlogLink(blog_name){

    blog_directory = "/Essays/blogs/"+language_set+"/";

    window.open(blog_directory + blog_name, "_self","", false);


}