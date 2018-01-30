/* Courtesy of https://github.com/codrops/ModalWindowEffects for effects and JS */

function getFocus() {
    // This is to gain focus on the modal click
    setTimeout(function () {
        document.getElementById("encryption-password").focus(); }, 250);
}

function checkForPassword() {
	var encryptForm = document.getElementById("encryption-password");

	if ( encryptForm.value === "" ) {
		var icon = document.getElementById("status-icon");
		var dataElement = icon.getAttribute("data");
		if ( !dataElement.endsWith("145-unlocked.svg") ) {
			var unlockedIcon = dataElement.replace("144-lock.svg", "145-unlocked.svg");
			icon.setAttribute("data", unlockedIcon);
		}
	}

	else {
		var icon = document.getElementById("status-icon");
		var dataElement = icon.getAttribute("data");
		if ( !dataElement.endsWith("144-lock.svg") ) {
			var lockIcon = dataElement.replace("145-unlocked.svg", "144-lock.svg");
			icon.setAttribute("data", lockIcon);
		}
	}
}

function classReg( className ) {
  return new RegExp("(^|\\s+)" + className + "(\\s+|$)");
}

var hasClass = function( elem, c ) {
    return classReg( c ).test( elem.className );
};

var addClass = function( elem, c ) {
    if ( !hasClass( elem, c ) ) {
        elem.className = elem.className + ' ' + c;
    }
};

var removeClass = function( elem, c ) {
    elem.className = elem.className.replace( classReg( c ), ' ' );
};

var ModalEffects = (function() {

	function init() {

		var overlay = document.querySelector( '.md-overlay' );

		[].slice.call( document.querySelectorAll( '.md-trigger' ) ).forEach( function( el, i ) {

			var modal = document.querySelector( '#' + el.getAttribute( 'data-modal' ) ),
				close = modal.querySelector( '.close' ),
				okay = modal.querySelector( '#okay-btn' ),
				input = modal.querySelector( '#encryption-password' );

			function removeModal( hasPerspective ) {
				removeClass( modal, 'md-show' );
				removeClass( overlay, 'md-show' );
			}

            function removeModalHandler() {
				removeModal( hasClass( el, 'md-setperspective' ) );
				checkForPassword();
			}

			el.addEventListener( 'click', function( ev ) {
				addClass( modal, 'md-show' );
                addClass( overlay, 'md-show' );
                getFocus();
				overlay.removeEventListener( 'click', removeModalHandler );
				overlay.addEventListener( 'click', removeModalHandler );
			});

			close.addEventListener( 'click', function( ev ) {
				ev.stopPropagation();
                removeModalHandler();
			});

			okay.addEventListener( 'click', function( ev ) {
				ev.stopPropagation();
                removeModalHandler();
			});

			input.addEventListener( 'keydown', function( ev ) {
				if (ev.key === "Enter") {
					ev.preventDefault();
					ev.stopPropagation();
					removeModalHandler();
				}
			});

		} );

	}

	init();

})();
