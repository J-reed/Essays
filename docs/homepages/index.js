

var language_set = "";


var blog_directory = "/Essays/blogs/English/";

function check_lang(){

    lang = document.getElementById("language_dropbox").value;

    switch(lang){
        case "Lang.ENGLISH":
            language_set = "English";
            break;
        case "Lang.FRENCH":
            language_set = "French";
            break;
        default:
            language_set = "English";
    }

}

function getBlogLink(blog_name){

    blog_directory = "/Essays/blogs/"+language_set+"/";

    window.open(blog_directory + blog_name, "_self","", false);


}