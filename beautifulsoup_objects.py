"""
saving html to file on machine

working with beautifulsoup objects
"""
from bs4 import BeautifulSoup

html_doc= """
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>PROMITHEAS</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link href="https://fonts.googleapis.com/css?family=Montserrat:200,300,400,500,600,700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="css/open-iconic-bootstrap.min.css">
    <link rel="stylesheet" href="css/animate.css">

    <link rel="stylesheet" href="css/owl.carousel.min.css">
    <link rel="stylesheet" href="css/owl.theme.default.min.css">
    <link rel="stylesheet" href="css/magnific-popup.css">

    <link rel="stylesheet" href="css/aos.css">

    <link rel="stylesheet" href="css/ionicons.min.css">

    <link rel="stylesheet" href="css/bootstrap-datepicker.css">
    <link rel="stylesheet" href="css/jquery.timepicker.css">


    <link rel="stylesheet" href="css/flaticon.css">
    <link rel="stylesheet" href="css/icomoon.css">
    <link rel="stylesheet" href="css/style.css">
  </head>
  <body>

	<div id="colorlib-page">
		<a href="#" class="js-colorlib-nav-toggle colorlib-nav-toggle"><i></i></a>
		<aside id="colorlib-aside" role="complementary" class="js-fullheight">
			<nav id="colorlib-main-menu" role="navigation">
				<ul>
					<li class="colorlib-active"><a href="index.html">Home</a></li>
					<li><a href="collection.html">Portfolio</a></li>
					<li><a href="about.html">About</a></li>
					<li><a href="services.html">Services</a></li>
					<!--  <li><a href="blog.html">Blog</a></li> -->
					<li><a href="contact.html">Contact</a></li>
				</ul>
				<!--  <p class="social">
					<span><a href="#">Facebook</a></span>
					<span><a href="#">Twitter</a></span>
					<span><a href="#">Instagram</a></span>
				</p>-->
			</nav>


		</aside> <!-- END COLORLIB-ASIDE -->
		<div id="colorlib-main">
			<section class="ftco-section ftco-no-pt ftco-no-pb mb-5 ftco-intro">
				<div class="container-fluid px-3 px-md-0">
					<div class="row justify-content-end">
						<div class="col-md-10 mt-3">
							<h1 class="mb-5"  style="color: #b82441">Promitheas</h1>
							<div class="row">
								<div class="col-md-6">

									<h3 another-attribute="mobile" class="web" >website design, web hosting, domain name registration, information technology blog.</h3>

								</div>
							</div>
						</div>
					</div>
				</div>
			</section>

			<section class="ftco-section ftco-no-pt ftco-counter img" id="section-counter">
	    	<div class="container-fluid px-3 px-md-0">
	    		<div class="row d-md-flex align-items-center justify-content-end">
	    			<div class="col-md-10">
	    				<div class="row d-md-flex align-items-start">
			          <div class="col-md d-flex justify-content-center counter-wrap ftco-animate">
			            <div class="block-18">
			              <div class="text">
			                <strong class="number" data-number="3">0</strong>
			                <span>Years of Experience</span>
			              </div>
			            </div>
			          </div>
			          <!--  <div class="col-md d-flex justify-content-center counter-wrap ftco-animate">
			            <div class="block-18">
			              <div class="text">
			                <strong class="number" data-number="2">0</strong>
			                <span>Happy Clients</span>
			              </div>
			            </div>
			          </div>-->
			          <div class="col-md d-flex justify-content-center counter-wrap ftco-animate">
			            <div class="block-18">
			              <div class="text">
			                <strong class="number" data-number="2">0</strong>
			                <span>Finished Projects</span>
			              </div>
			            </div>
			          </div>
			          <div class="col-md d-flex justify-content-center counter-wrap ftco-animate">
			            <div class="block-18">
			              <div class="text">
			                <strong class="number" data-number="300">0</strong>
			                <span class="web" another-attribute="web2">Working Days</span>
			              </div>
			            </div>
			          </div>
		          </div>
	          </div>
	        </div>
	    	</div>
	    </section>




      <footer class="ftco-footer ftco-bg-dark ftco-section" style="background: #004084">
        <div class="container px-md-5">
          <div class="row mb-5">

            <div class="col-md">
               <div class="ftco-footer-widget mb-4 pl-lg-5">
                <h2 class="ftco-heading-2">Links</h2>
                <ul class="list-unstyled categories">
                  <li><a href="home.html">Home</a></li>
                  <li><a href="about.html">About</a></li>
                  <li><a href="portfolio.html">Portfolio</a></li>
                  <li><a href="services.html">Services</a></li>
                  <!--  <li><a href="blog.html">Blog</a></li> -->
                  <li><a href="contact.html">Contact</a></li>
                </ul>
              </div>
            </div>

            <div class="col-md">
              <div class="ftco-footer-widget mb-4">
                <h2 class="ftco-heading-2">Have a Questions?</h2>
                <div class="block-23 mb-3">
                  <ul>
                    <li><span class="icon icon-map-marker"></span><span class="text">Kampala, Uganda</span></li>
                    <li><a href="tel://+256703206867"><span class="icon icon-phone"></span><span class="text">+256703206867</span></a></li>
                    <li><a href="mailto:matthieumuchu@gmail.com"><span class="icon icon-envelope"></span><span class="text">matthieumuchu@gmail.com</span></a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">

              <p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
    Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="icon-heart" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
    <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
            </div>
          </div>
        </div>
      </footer>
		</div><!-- END COLORLIB-MAIN -->
	</div><!-- END COLORLIB-PAGE -->

  <!-- loader -->
  <div id="ftco-loader" class="show fullscreen"><svg class="circular" width="48px" height="48px"><circle class="path-bg" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke="#eeeeee"/><circle class="path" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke-miterlimit="10" stroke="#F96D00"/></svg></div>


  <script src="js/jquery.min.js"></script>
  <script src="js/jquery-migrate-3.0.1.min.js"></script>
  <script src="js/popper.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  <script src="js/jquery.easing.1.3.js"></script>
  <script src="js/jquery.waypoints.min.js"></script>
  <script src="js/jquery.stellar.min.js"></script>
  <script src="js/owl.carousel.min.js"></script>
  <script src="js/jquery.magnific-popup.min.js"></script>
  <script src="js/aos.js"></script>
  <script src="js/jquery.animateNumber.min.js"></script>
  <script src="js/jquery.mb.YTPlayer.min.js"></script>
  <script src="js/scrollax.min.js"></script>
  <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBVWaKrjvy3MaE7SQ74_uJiULgl1JY0H2s&sensor=false"></script>
  <script src="js/google-map.js"></script>
  <script src="js/main.js"></script>

  </body>
</html>


"""

with open('index.html', 'w') as f:
    f.write(html_doc)

soup= BeautifulSoup(html_doc, 'lxml')

#print(soup.prettify())

#print(soup)

print(soup.h3) #prints out first occurrence of the h3 tag
#print(soup.find('h3')) #prints out first occurrence of the h3 tag
print(soup.find_all('p')) #prints out all occurrences of p a_tag

print(soup.h3.name) #prints name of the tag

#we can alter the name and have it reflected in the source and the tag in the source changes e.g h3 to h1
tag = soup.h3
print(tag)
tag.name="h1"
print(tag)

#writing index2.html to file to show changes of the h3 tag to h1
index2=soup.prettify()

with open('index2.html', 'w') as f:
    f.write(index2)

tag2= soup.find_all('span')[2] #prints out the second index of the list of p tags throughout the html document provided
print(tag2)

#getting a specific attribute on the tag
print(tag['class'])
print(tag['another-attribute'])

#if we want to see all attributes, we can access them as a dictionary object
tag2= soup.find_all('span')[2]
print(tag2.attrs)

#tag= soup.find('h1')
#print(tag)
#print(tag.attrs)

#altering attributes using BeautifulSoup
tag2['class']= 3
print(tag2)

# we can use del command for lists to remove attributes
del tag2['another-attribute']
print(tag2)

#we can get the string between the html tags like This
print(tag2.string)

#we can use replace_with method after string method to change the content between the html tags
tag2.string.replace_with("Working Years")
print(tag2)
