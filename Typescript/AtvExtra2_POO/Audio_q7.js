/*
7. Implemente a questão do ControleDeAudio acima em outra linguagem que não
seja TypeScript.

**/ 

var ControleDeAudio = /** @class */ (function () {
    function ControleDeAudio() {
        this.volume = 0;
    }
    ControleDeAudio.prototype.AumentarVolume = function () {
        if (this.volume > 10) {
            return this.volume = 10;
        }
        else {
            return this.volume += 1;
        }
    };
    ControleDeAudio.prototype.DiminuirVolume = function () {
        if (this.volume < 0) {
            return this.volume = 0;
        }
        else {
            return this.volume -= 1;
        }
    };
    ControleDeAudio.prototype.LerVolume = function () {
        return this.volume;
    };
    return ControleDeAudio;
}());
var controle = new ControleDeAudio();
controle.volume = 2;
console.log("Volume aumentado para: " + controle.AumentarVolume());
console.log("Volume diminuido para: " + controle.DiminuirVolume());
console.log("Volume agora: " + controle.LerVolume());
