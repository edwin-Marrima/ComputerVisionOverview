var webdriver = require("selenium-webdriver");
var By = require("selenium-webdriver").By;
var until = require("selenium-webdriver").until;


var driver = new webdriver.Builder().forBrowser('chrome').build();
driver.manage().window().maximize();


//driver.manage().deleteAllcookies();

driver.get('https://www.facebook.com');

//driver.findElement(By.name('q')).sendKeys('lucassantosbras');
//driver.findElement(By.name('.gNO89b')).click();

//driver.findElement(By.name('email')).sendKeys('848564695');
//driver.findElement(By.name('pass')).sendKeys('840233996');
var eu = driver.findElement(By.name('firstname'));
driver.findElement(By.name('firstname')).sendKeys('Amelia ');

driver.findElement(By.name('lastname')).sendKeys('Batista');
driver.findElement(By.name('reg_email__')).sendKeys('eduardo1234@gmail.com');
driver.findElement(By.name('reg_email_confirmation__')).sendKeys('eduardo1234@gmail.com');
driver.findElement(By.name('reg_passwd__')).sendKeys('Maria7744');
driver.findElement(By.name('birthday_month')).click();

driver.findElement(By.id('u_0_8')).click();
//
//driver.findElement(By.linkText('u_0_8')).click();

console.log("eyeye");
driver.findElement(By.xpath('//*[@id="u_0_y"]')).click();

//driver.findElement(By.xpath('//*[@id="u_0_2"]')).click();
//driver.findElement(By.css('._1frb'));
//driver.findElement(By.css('._1frb')).sendKeys('parafernalhaaa');


//driver.findElement(By.xpath('//*[@id="u_0_a"]/div[1]/div[1]/div/a')).click();
//var promise = driver.findElement(By.css('.domain')).getText();
//promise.then(function(title){
//console.log('vuvud:' + title);
//});

//driver.findElement(By.css('.title')).then(function(txt) {
//  console.log("o valor  eh:"+txt);
//});



//btnk
//driver.sleep(10000);
//driver.quit();


//var eu = driver.findElement(By.xpath('//*[@id="u_0_a"]')).getText();
//eu.then(function(texto){
//  console.log('eh o caraa: ' + texto);
//});
