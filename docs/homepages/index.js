

var language_set = "";


var blog_directory = "/Essays/blogs/English/";

function check_lang(){

    lang = document.getElementById("language_dropbox").value;

    switch(lang){
        case "Lang.ENGLISH":
            language = "English";
            break;
        case "Lang.FRENCH":
            language = "French";
            break;
        default:
            language = "English";
    }

    return language;
}

function getBlogLink(blog_name){

    blog_directory = "/Essays/blogs/"+language_set+"/";

    window.open(blog_directory + blog_name, "_self","", false);


}