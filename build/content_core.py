# -*- coding: utf-8 -*-
"""Core pages: home, about, experience, work index, skills, contact."""

HOME = """
  <!-- HERO -->
  <section class="hero">
    <div class="wrap">
      <div class="hero-topline mono">
        <span><span class="dot" aria-hidden="true"></span>Portfolio / Operations &amp; Program Management</span>
        <span class="hide-sm">Early-career professional</span>
      </div>

      <div class="hero-grid">
        <div>
          <h1>
            <span class="line">A little <em>structure.</em></span>
            <span class="line">A lot of <em class="ink">forward motion.</em></span>
          </h1>

          <div class="hero-lede">
            <p>I&rsquo;m Shailly, an operations and program management professional interested in turning ideas, moving parts, and messy processes into organised, executable work.</p>
            <p>I like understanding how things work, figuring out where they break, and building better ways to move them forward.</p>
          </div>

          <div class="hero-descriptor mono">
            <span>Operations</span><span class="sep" aria-hidden="true">/</span>
            <span>Program Management</span><span class="sep" aria-hidden="true">/</span>
            <span>Process Improvement</span>
          </div>

          <div class="hero-actions">
            <a class="btn" href="/work/">Explore My Work <span class="arrow" aria-hidden="true">&rarr;</span></a>
            <a class="btn btn--ghost" href="/contact/">Get in Touch</a>
          </div>
        </div>

        <aside class="op-card reveal" aria-label="How I read a piece of work">
          <div class="op-head mono">
            <span>Operating layers</span>
            <span class="live"><i aria-hidden="true"></i>In motion</span>
          </div>
          <div class="op-layers">
            <div class="op-layer">
              <span class="num">01</span>
              <span>
                <span class="lbl">People</span>
                <span class="desc">Who needs to be involved, and what they own.</span>
              </span>
              <span class="bar" aria-hidden="true"><i class="on"></i><i class="on"></i><i></i><i></i></span>
            </div>
            <div class="op-layer">
              <span class="num">02</span>
              <span>
                <span class="lbl">Process</span>
                <span class="desc">What needs to happen, in what order.</span>
              </span>
              <span class="bar" aria-hidden="true"><i class="on"></i><i class="on"></i><i class="on"></i><i></i></span>
            </div>
            <div class="op-layer">
              <span class="num">03</span>
              <span>
                <span class="lbl">Communication</span>
                <span class="desc">Where handoffs and follow-ups can break.</span>
              </span>
              <span class="bar" aria-hidden="true"><i class="on"></i><i></i><i></i><i></i></span>
            </div>
            <div class="op-layer">
              <span class="num">04</span>
              <span>
                <span class="lbl">Execution</span>
                <span class="desc">How the work actually gets moved forward.</span>
              </span>
              <span class="bar" aria-hidden="true"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i></span>
            </div>
          </div>
          <div class="op-foot mono">
            <span>Built for moving parts</span>
            <span>Fig. 01</span>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <!-- STRIP -->
  <div class="strip" aria-hidden="true">
    <div class="strip-track">
      <div class="strip-group mono">
        <span>Workflow design</span><i></i><span>Recruitment &amp; onboarding</span><i></i><span>Program coordination</span><i></i><span>Process documentation</span><i></i><span>Stakeholder communication</span><i></i><span>Educational initiatives</span><i></i><span>Follow-through</span><i></i>
      </div>
      <div class="strip-group mono">
        <span>Workflow design</span><i></i><span>Recruitment &amp; onboarding</span><i></i><span>Program coordination</span><i></i><span>Process documentation</span><i></i><span>Stakeholder communication</span><i></i><span>Educational initiatives</span><i></i><span>Follow-through</span><i></i>
      </div>
    </div>
  </div>

  <!-- INTRODUCTION -->
  <section class="section" id="approach">
    <div class="wrap split">
      <div class="split-sticky reveal">
        <p class="kicker mono">01 / Approach</p>
        <h2>I pay attention to the things that <em>make the work work.</em></h2>
      </div>

      <div class="reveal" style="--d:.08s">
        <div class="split-copy">
          <p class="lead-p">Every initiative has the visible part: the event, the program, the launch, the outcome.</p>
          <p>Then there&rsquo;s everything underneath it. The coordination, follow-ups, documentation, timelines, people, decisions, and processes that make the visible part possible.</p>
          <p>That&rsquo;s the part of the work I find interesting.</p>
          <p>My experience has taken me through content development, team coordination, program operations, recruitment, onboarding, and educational initiatives.</p>
          <p>Across these environments, I&rsquo;ve developed an interest in understanding how work moves through an organisation&mdash;and what can make that process more effective.</p>
        </div>

        <div class="layers" aria-label="The visible part of a project and the layers underneath it">
          <div class="layer-visible">
            <div>
              <span class="mono">The visible part</span><br>
              <strong>The program, the event, the launch, the outcome</strong>
            </div>
            <span class="mono">Surface</span>
          </div>
          <div class="layer-connector mono">
            <span class="line line--dash" aria-hidden="true"></span>
            <span>What sits underneath</span>
          </div>
          <div class="layer-stack">
            <div class="layer-item"><span class="n">01</span><span class="t">Coordination</span><span class="bar" aria-hidden="true"></span></div>
            <div class="layer-item"><span class="n">02</span><span class="t">Follow-ups</span><span class="bar" aria-hidden="true"></span></div>
            <div class="layer-item"><span class="n">03</span><span class="t">Documentation</span><span class="bar" aria-hidden="true"></span></div>
            <div class="layer-item"><span class="n">04</span><span class="t">Decisions</span><span class="bar" aria-hidden="true"></span></div>
            <div class="layer-item"><span class="n">05</span><span class="t">Processes</span><span class="bar" aria-hidden="true"></span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SELECTED WORK -->
  <section class="section section--tight" id="work">
    <div class="wrap">
      <div class="section-head reveal">
        <div>
          <p class="kicker mono">02 / Selected work</p>
          <h2>A few things I&rsquo;ve helped move forward.</h2>
        </div>
        <p class="head-copy">Four implemented projects, documented the way I try to run them: the situation, what was getting in the way, what changed, and what came out of it.</p>
      </div>

      <div class="work-list">
        <a class="work-row reveal" href="/work/recruitment-onboarding-workflow/" aria-label="Case study 01: Recruitment &amp; Onboarding Workflow Redesign">
          <span class="work-num">01</span>
          <div>
            <span class="work-cat mono">Operations / Process Improvement</span>
            <h3 class="work-title">Recruitment &amp; Onboarding Workflow Redesign</h3>
            <p class="work-desc">Redesigned a fragmented volunteer recruitment and onboarding process by consolidating application intake, introducing centralised candidate tracking, standardising communication, and creating clearer ownership across recruitment stages.</p>
          </div>
          <div class="work-meta">
            <span class="work-highlight">Interview scheduling improved from several weeks to under seven days</span>
            <span class="work-open">Case study <span aria-hidden="true">&nearr;</span></span>
          </div>
        </a>

        <a class="work-row reveal" href="/work/instagram-live-series/" aria-label="Case study 02: Instagram Live Series">
          <span class="work-num">02</span>
          <div>
            <span class="work-cat mono">Program Development / Volunteer Engagement</span>
            <h3 class="work-title">Instagram Live Series</h3>
            <p class="work-desc">Conceived and led a recurring Instagram Live initiative, coordinating speakers, preparing volunteers, developing session content, and managing execution across more than 10 sessions.</p>
          </div>
          <div class="work-meta">
            <span class="work-highlight">10+ sessions<br>15+ speakers</span>
            <span class="work-open">Case study <span aria-hidden="true">&nearr;</span></span>
          </div>
        </a>

        <a class="work-row reveal" href="/work/ending-the-period-stigma/" aria-label="Case study 03: Ending the Period Stigma">
          <span class="work-num">03</span>
          <div>
            <span class="work-cat mono">Program Strategy / Initiative Execution</span>
            <h3 class="work-title">Ending the Period Stigma</h3>
            <p class="work-desc">Conceptualised and led a research-based menstrual health awareness initiative, adapting its delivery approach into a collaborative campus exhibition.</p>
          </div>
          <div class="work-meta">
            <span class="work-highlight">70+ students engaged</span>
            <span class="work-open">Case study <span aria-hidden="true">&nearr;</span></span>
          </div>
        </a>

        <a class="work-row reveal" href="/work/menstrual-health-webinar/" aria-label="Case study 04: Menstrual Health Webinar">
          <span class="work-num">04</span>
          <div>
            <span class="work-cat mono">Program Coordination / Educational Content</span>
            <h3 class="work-title">Menstrual Health Webinar &mdash; Rotaract Club of Dyal Singh College &times; Project Aaina</h3>
            <p class="work-desc">Represented TPSR in a collaborative educational webinar on menstrual health. Contributed to content development, speaker preparation, event coordination, presentation flow, and audience moderation.</p>
          </div>
          <div class="work-meta">
            <span class="work-highlight">~50 attendees<br>6 roles</span>
            <span class="work-open">Case study <span aria-hidden="true">&nearr;</span></span>
          </div>
        </a>
      </div>

      <div style="margin-top:2rem" class="reveal">
        <a class="btn btn--ghost" href="/work/">See the full work index <span class="arrow" aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </section>

  <!-- BEYOND THE PROJECTS -->
  <section class="section band" id="samples">
    <div class="wrap">
      <div class="section-head reveal">
        <div>
          <p class="kicker mono">03 / Beyond the projects</p>
          <h2>Some of my work is best understood through the <em>artefacts themselves.</em></h2>
        </div>
        <p class="head-copy">Program frameworks, operational documents, data analysis, and planning assignments.</p>
      </div>

      <div class="sample-rows">
        <a class="sample-row reveal" href="/work/samples/kraftshala-assignment/">
          <div class="sr-visual" aria-hidden="true">
            <div class="doc-thumb doc-thumb--dash">
              <div class="dt-bar mono"><span>Week-on-week dashboard</span><span>Illustrative</span></div>
              <div class="dt-kpis">
                <div class="dt-kpi"><b>44%</b><span>On-time sessions</span></div>
                <div class="dt-kpi"><b>38%</b><span>&ldquo;Other&rdquo; cancellations</span></div>
                <div class="dt-kpi"><b>24.7</b><span>Avg. positive delay (min)</span></div>
              </div>
              <div class="dt-chart">
                <span style="--v:28%"></span><span style="--v:44%"></span><span style="--v:36%"></span>
                <span style="--v:72%"></span><span style="--v:58%"></span><span style="--v:88%"></span>
              </div>
            </div>
          </div>
          <div class="sr-body">
            <span class="mono sr-cat">Work sample 01 &middot; Independent &middot; Kraftshala Program Management assignment, 2026</span>
            <h3>Student Experience &amp; Operational Analytics</h3>
            <p>A two-part program management hiring assignment exploring student support, operational problem-solving, and data-driven decision-making.</p>
            <div class="sr-tags">
              <span class="pill">Four-scenario decision framework</span>
              <span class="pill">Operational analytics</span>
              <span class="pill">Excel workbook</span>
            </div>
            <span class="link-arrow">Open work sample <span aria-hidden="true">&nearr;</span></span>
          </div>
        </a>

        <a class="sample-row reveal" href="/work/samples/ui-fellowship-presentation/">
          <div class="sr-visual" aria-hidden="true">
            <div class="doc-thumb doc-thumb--deck">
              <div class="dt-slide">
                <span class="mono">Program design</span>
                <strong>Recruitment operating system</strong>
                <div class="dt-slide-nodes"><i></i><i></i><i></i><i></i></div>
              </div>
              <div class="dt-slide dt-slide--ghost">
                <span class="mono">Operating model</span>
                <div class="dt-slide-lines"><i></i><i></i><i></i></div>
              </div>
            </div>
          </div>
          <div class="sr-body">
            <span class="mono sr-cat">Work sample 02 &middot; Independent &middot; Hiring process presentation</span>
            <h3>U&amp;I Fellowship &mdash; Program Design &amp; Recruitment Operations</h3>
            <p>How a fellowship program could structure its recruitment and operating model: venue partnership proposal, recruitment leadership structure, operating system, coordination framework, and timelines.</p>
            <div class="sr-tags">
              <span class="pill">Recruitment operating system</span>
              <span class="pill">Coordination framework</span>
              <span class="pill">Timelines</span>
            </div>
            <span class="link-arrow">Open work sample <span aria-hidden="true">&nearr;</span></span>
          </div>
        </a>
      </div>

      <div style="margin-top:2rem" class="reveal">
        <a class="btn btn--ghost" href="/work/#samples">All work samples &amp; documents <span class="arrow" aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </section>

  <!-- EXPERIENCE PREVIEW -->
  <section class="section" id="experience" style="border-top:1px solid var(--line)">
    <div class="wrap">
      <div class="section-head reveal">
        <div>
          <p class="kicker mono">04 / Experience</p>
          <h2>Where I&rsquo;ve worked. What I&rsquo;ve worked on.</h2>
        </div>
        <p class="head-copy">A high-volume, target-driven EdTech environment and a volunteer-led organisation with more than 50 volunteers &mdash; plus earlier work in content, research, and fundraising.</p>
      </div>

      <div class="xp-list">
        <article class="xp reveal">
          <div class="xp-date mono">
            <span>Aug 2026 &mdash; Present</span>
            <span class="now">Current</span>
          </div>
          <div class="xp-body">
            <h3>Academic Counselor</h3>
            <p class="xp-org">Vedantu</p>
            <p>Working across the student and parent interaction lifecycle, from initial enquiry through demos and enrollment. Maintaining structured lead records, managing follow-ups, coordinating internal handoffs, and monitoring progress in a high-volume EdTech environment.</p>
          </div>
        </article>

        <article class="xp reveal">
          <div class="xp-date mono">
            <span>Feb 2021 &mdash; Oct 2024</span>
          </div>
          <div class="xp-body">
            <h3>Program Operations Coordinator &amp; Organisational Mentor</h3>
            <p class="xp-org">The Period Society Rajasthan</p>
            <p>Worked across program operations, recruitment, onboarding, organisational systems, educational initiatives, and content operations in a volunteer-led organisation with more than 50 volunteers.</p>
            <p class="xp-note">Responsibilities also included concurrent roles as Head of Content and Social Media Manager.</p>
          </div>
        </article>
      </div>

      <div class="xp-compact reveal">
        <span class="mono xp-compact-label">Earlier</span>
        <div class="xp-compact-items">
          <span>Freelance Copywriter</span>
          <span>Broxer &middot; Content Writer</span>
          <span>Affnosys India &middot; Content Writer</span>
          <span>JMES &middot; Business Development Intern</span>
        </div>
      </div>

      <div style="margin-top:2rem" class="reveal">
        <a class="btn btn--ghost" href="/experience/">View full experience <span class="arrow" aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="cta-band">
    <div class="wrap cta-grid">
      <div class="reveal">
        <p class="kicker mono">05 / Next</p>
        <h2>Good work needs <em>good systems.</em></h2>
      </div>
      <div class="reveal" style="--d:.08s">
        <p class="cta-copy">I&rsquo;m interested in opportunities where I can contribute to program execution, operational improvement, and building systems that help teams work better.</p>
        <a class="btn btn--light" href="/contact/">Let&rsquo;s Connect <span class="arrow" aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </section>
"""

ABOUT = """
  <section class="page-head">
    <div class="wrap">
      <nav class="breadcrumb mono" aria-label="Breadcrumb">
        <a href="/">Home</a><span class="sep" aria-hidden="true">/</span><span>About</span>
      </nav>
      <div class="page-head-grid">
        <div>
          <h1>A little about <em>how I work.</em></h1>
          <div class="page-lede">
            <p>I&rsquo;m drawn to the space between an idea and its execution.</p>
          </div>
        </div>
        <div class="head-fact reveal">
          <span class="mono">At a glance</span>
          <dl>
            <dt class="mono">Focus</dt>
            <dd>Operations &middot; Program management &middot; Process improvement</dd>
            <dt class="mono">Environments</dt>
            <dd>Volunteer-led organisations &middot; Education &middot; Content operations &middot; Program delivery</dd>
            <dt class="mono">Based</dt>
            <dd>India &middot; Open to remote and on-site roles</dd>
          </dl>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap split">
      <div class="split-sticky reveal">
        <p class="kicker mono">01 / Perspective</p>
        <h2>Understanding how the pieces <em>fit together.</em></h2>
      </div>
      <div class="reveal" style="--d:.08s">
        <div class="prose">
          <p class="lead">I like understanding how different pieces fit together: who needs to be involved, what needs to happen, where communication can break down, and what systems would make the process easier to manage.</p>
          <p>My professional experience began with content, research, and educational work. Over time, I took on responsibilities involving team coordination, program execution, recruitment, onboarding, and organisational operations.</p>
          <p>Working in environments where people wear multiple hats and resources are limited taught me to look beyond the immediate task and pay attention to the systems around it.</p>
          <p>I enjoy work that involves both thinking and doing: understanding a problem, developing a better approach, and putting that approach into practice.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight" style="border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:var(--paper)">
    <div class="wrap">
      <div class="section-head reveal">
        <div>
          <p class="kicker mono">02 / How I approach work</p>
          <h2>Four habits that show up in <em>everything I run.</em></h2>
        </div>
        <p class="head-copy">These are the things I keep coming back to, whether the work is a recruitment process, an event, a document set, or a tracker.</p>
      </div>

      <div class="principles">
        <article class="principle reveal">
          <span class="pnum mono">01</span>
          <h3>Structure from ambiguity</h3>
          <p>I enjoy taking situations that feel scattered and making them easier to understand. That might mean mapping a workflow, creating a tracker, clarifying responsibilities, or figuring out what needs to happen next.</p>
        </article>
        <article class="principle reveal">
          <span class="pnum mono">02</span>
          <h3>People and coordination</h3>
          <p>Execution rarely happens in isolation. I pay attention to communication, dependencies, handoffs, and the different people involved in getting something done.</p>
        </article>
        <article class="principle reveal">
          <span class="pnum mono">03</span>
          <h3>Systems that actually work</h3>
          <p>I like building practical systems that people can use consistently. Documentation, trackers, templates, guidelines, and repeatable workflows make work easier to manage.</p>
        </article>
        <article class="principle reveal">
          <span class="pnum mono">04</span>
          <h3>Ownership and follow-through</h3>
          <p>I pay attention to what is falling through the cracks, what needs a follow-up, and where someone needs to step in to keep things moving.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
        <div class="personal reveal">
          <p class="kicker mono kicker--plain">03 / A little beyond work</p>
          <h2>Curious about how things work.</h2>
          <p>I am naturally curious about how things work. I enjoy researching, understanding problems from different angles, and connecting ideas that might initially seem unrelated.</p>
          <p>I appreciate work that involves both analysis and execution.</p>
        </div>
        <div class="fact-rail reveal">
          <div class="fact">
            <span class="k mono">Background</span>
            <span class="v">Content, research, and educational work first; operations, recruitment, and program delivery next.</span>
          </div>
          <div class="fact">
            <span class="k mono">Environments</span>
            <span class="v">Volunteer-led organisations, education, content operations, and program environments.</span>
          </div>
          <div class="fact">
            <span class="k mono">Working style</span>
            <span class="v">Understand the problem, bring clarity to the moving parts, build a workable system, follow through.</span>
          </div>
        </div>
    </div>
  </section>

  <section class="cta-band">
    <div class="wrap cta-grid">
      <div class="reveal">
        <p class="kicker mono">Next</p>
        <h2>Want the evidence, <em>not the summary?</em></h2>
      </div>
      <div class="reveal" style="--d:.08s">
        <p class="cta-copy">The selected work section documents four projects, from the problem through to what changed.</p>
        <a class="btn btn--light" href="/work/">Explore the work <span class="arrow" aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </section>
"""

EXPERIENCE = """
  <section class="page-head">
    <div class="wrap">
      <nav class="breadcrumb mono" aria-label="Breadcrumb">
        <a href="/">Home</a><span class="sep" aria-hidden="true">/</span><span>Experience</span>
      </nav>
      <div class="page-head-grid">
        <div>
          <h1>Work that involved <em>moving parts.</em></h1>
          <div class="page-lede">
            <p>A progression from content, research, and educational work into program operations, recruitment, onboarding, and organisational systems.</p>
          </div>
        </div>
        <div class="head-fact reveal">
          <span class="mono">Overview</span>
          <dl>
            <dt class="mono">Current</dt>
            <dd>Academic Counselor &middot; Vedantu &middot; Aug 2026 &mdash; Present</dd>
            <dt class="mono">Longest</dt>
            <dd>Program Operations Coordinator &amp; Organisational Mentor &middot; The Period Society Rajasthan &middot; Feb 2021 &mdash; Oct 2024</dd>
            <dt class="mono">Also</dt>
            <dd>Head of Content &middot; Social Media Manager &middot; content and copywriting roles &middot; one-week fundraising internship</dd>
          </dl>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">

      <!-- VEDANTU -->
      <article class="role-block reveal">
        <header class="role-head">
          <div>
            <h2>Vedantu</h2>
            <p class="role-sub">Academic Counselor</p>
          </div>
          <p class="role-when mono"><strong>Aug 2026 &mdash; Present</strong><span class="now">Current</span></p>
        </header>
        <div class="role-body">
          <div class="prose">
            <p class="lead">Working across the student and parent interaction lifecycle, from initial enquiry through demos and enrollment.</p>
            <p>My role involves maintaining structured lead records, managing follow-ups, coordinating internal handoffs, and monitoring progress in a high-volume EdTech environment.</p>
          </div>
          <div>
            <p class="resp-title mono">Responsibilities</p>
            <ul class="resp">
              <li>Manage student and parent interactions throughout the enquiry, demo, and enrollment journey.</li>
              <li>Maintain follow-ups, lead statuses, and interaction records using Google Sheets, LeadSquared, and MCUBE.</li>
              <li>Coordinate with Master Teachers, Demo, Onboarding, and Operations teams to support continuity across the learner journey.</li>
              <li>Monitor lead progress and daily performance against individual targets.</li>
            </ul>
          </div>
        </div>
      </article>

      <!-- TPSR -->
      <article class="role-block role-block--org reveal">
        <header class="role-head">
          <div>
            <h2>The Period Society Rajasthan</h2>
            <p class="role-sub">Program Operations Coordinator &amp; Organisational Mentor &middot; Head of Content &middot; Social Media Manager</p>
          </div>
          <p class="role-when mono"><strong>Feb 2021 &mdash; Oct 2024</strong></p>
        </header>
        <div class="role-body">
          <div class="prose">
            <p class="lead">The Period Society Rajasthan was a volunteer-led organisation working on menstrual health education and awareness, with more than 50 volunteers.</p>
            <p>My responsibilities evolved over time across content, social media, program operations, organisational systems, recruitment, onboarding, and educational initiatives.</p>
          </div>

          <div class="role-track">
            <div class="rt-line" aria-hidden="true"></div>

            <section class="rt-role">
              <header class="rt-head">
                <span class="rt-dot" aria-hidden="true"></span>
                <h3>Program Operations Coordinator &amp; Organisational Mentor</h3>
                <span class="rt-when mono">Feb 2021 &mdash; Oct 2024</span>
              </header>
              <ul class="resp">
                <li>Redesigned recruitment and interview workflows.</li>
                <li>Introduced centralised candidate tracking and standardised communication templates.</li>
                <li>Developed onboarding processes and tracked volunteer documentation and orientation.</li>
                <li>Built organisational systems, including policies, codes of conduct, volunteer agreements, MOAs, and process documentation.</li>
                <li>Coordinated multiple concurrent initiatives.</li>
                <li>Managed follow-ups, meetings, action items, and communication with leadership and department heads.</li>
                <li>Created project trackers to monitor tasks, timelines, and progress.</li>
                <li>Developed educational resources and supported more than 30 educational initiatives.</li>
              </ul>
            </section>

            <section class="rt-role">
              <header class="rt-head">
                <span class="rt-dot" aria-hidden="true"></span>
                <h3>Head of Content</h3>
                <span class="rt-when mono">Concurrent role</span>
              </header>
              <div class="prose">
                <p>Led content operations and educational content development, coordinating a team of more than 20 members.</p>
              </div>
              <ul class="resp">
                <li>Led and coordinated the content team.</li>
                <li>Developed educational content frameworks.</li>
                <li>Managed content planning and review workflows.</li>
                <li>Coordinated publishing schedules and cross-functional content requirements.</li>
                <li>Supported research, curriculum development, and educational resource creation.</li>
              </ul>
            </section>

            <section class="rt-role">
              <header class="rt-head">
                <span class="rt-dot" aria-hidden="true"></span>
                <h3>Social Media Manager</h3>
                <span class="rt-when mono">Concurrent role</span>
              </header>
              <div class="prose">
                <p>Managed social media operations and content publishing, supporting the organisation&rsquo;s communication and audience engagement.</p>
              </div>
              <ul class="resp">
                <li>Managed Instagram content and publishing workflows.</li>
                <li>Coordinated with design and content teams.</li>
                <li>Supported social media campaigns and educational communication.</li>
                <li>Worked on speaker promotion and event-related content.</li>
              </ul>
            </section>
          </div>
        </div>
      </article>

      <!-- EARLIER -->
      <article class="role-block role-block--earlier reveal">
        <header class="role-head">
          <div>
            <h2>Earlier roles</h2>
            <p class="role-sub">Content, copywriting, and business development</p>
          </div>
        </header>
        <div class="role-body">
          <div>
          <p class="resp-title mono">Experience</p>
          <ul class="role-list">
            <li>
              <div class="rl-head"><h3>Freelance Copywriter</h3><span class="mono rl-when">Freelance</span></div>
              <p>Repurposed long-form podcast conversations into written articles for an American audience.</p>
            </li>
            <li>
              <div class="rl-head"><h3>Content Writer</h3><span class="mono rl-when">Broxer</span></div>
              <p>Researched, translated, and produced more than five daily news and infotainment scripts.</p>
            </li>
            <li>
              <div class="rl-head"><h3>Content Writer</h3><span class="mono rl-when">Affnosys India</span></div>
              <p>Worked on research-based, SEO-focused writing and digital content development.</p>
            </li>
            <li>
              <div class="rl-head"><h3>Business Development (Fundraising &amp; Strategies Development) Intern</h3><span class="mono rl-when">JMES &middot; May 7&ndash;14, 2022</span></div>
              <p>Completed a one-week internship involving fundraising and strategy development. Contributed to fundraising activities for the SHIKSHA project, strategy development, and interdepartmental coordination.</p>
            </li>
          </ul>
          </div>
        </div>
      </article>

      <!-- EDUCATION -->
      <article class="role-block role-block--edu reveal">
        <header class="role-head">
          <div>
            <h2>Education</h2>
            <p class="role-sub">Formal qualifications</p>
          </div>
        </header>
        <div class="role-body">
          <div class="edu-table" role="table" aria-label="Education history">
            <div class="edu-row" role="row">
              <span class="qual" role="cell">Bachelor of Arts</span>
              <span class="inst" role="cell">Panjab University, Chandigarh</span>
              <span class="yr mono" role="cell">2023 &mdash; 2026</span>
            </div>
            <div class="edu-row" role="row">
              <span class="qual" role="cell">Bachelor of Arts</span>
              <span class="inst" role="cell">CHRIST University, Bengaluru</span>
              <span class="yr mono" role="cell">2021 &mdash; 2023</span>
            </div>
            <div class="edu-row" role="row">
              <span class="qual" role="cell">Class XII &mdash; CBSE</span>
              <span class="inst" role="cell">Welham Girls&rsquo; School, Dehradun</span>
              <span class="yr mono" role="cell">2021</span>
              <span class="score mono" role="cell">95.5%</span>
            </div>
            <div class="edu-row" role="row">
              <span class="qual" role="cell">Class X &mdash; CBSE</span>
              <span class="inst" role="cell">Delhi Public School, Jodhpur</span>
              <span class="yr mono" role="cell">2019</span>
              <span class="score mono" role="cell">90.8%</span>
            </div>
          </div>
        </div>
      </article>

      <div class="reveal" style="margin-top:2.5rem">
        <a class="btn btn--ghost" href="/work/">See how this work translated into projects <span class="arrow" aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </section>
"""

WORK_INDEX = """
  <section class="page-head">
    <div class="wrap">
      <nav class="breadcrumb mono" aria-label="Breadcrumb">
        <a href="/">Home</a><span class="sep" aria-hidden="true">/</span><span>Selected Work</span>
      </nav>
      <div class="page-head-grid">
        <div>
          <h1>Work that had to <em>actually happen.</em></h1>
          <div class="page-lede">
            <p>Implemented projects sit at the centre. Around them: independent work samples and organisational documents that show how I approach problems.</p>
          </div>
        </div>
        <div class="head-fact reveal">
          <span class="mono">Index</span>
          <dl>
            <dt class="mono">Implemented projects</dt>
            <dd>04</dd>
            <dt class="mono">Independent work samples</dt>
            <dd>02</dd>
            <dt class="mono">Organisational documents</dt>
            <dd>02</dd>
          </dl>
        </div>
      </div>
    </div>
  </section>

  <!-- IMPLEMENTED -->
  <section class="section section--tight" id="projects" aria-labelledby="projects-h">
    <div class="wrap">
      <div class="section-head reveal">
        <div>
          <p class="kicker mono">A / Implemented projects</p>
          <h2 id="projects-h">Carried out inside an organisation.</h2>
        </div>
        <p class="head-copy">Each of these was delivered in a real setting, with real constraints, people, and follow-through. Written as context, problem, approach, execution, outcomes, reflection.</p>
      </div>

      <div class="case-grid">
        <a class="case-card reveal" href="/work/recruitment-onboarding-workflow/" aria-label="Case study 01: Recruitment &amp; Onboarding Workflow Redesign">
          <span class="cc-num">01</span>
          <div>
            <span class="cc-cat mono">Operations / Process Improvement &middot; The Period Society Rajasthan</span>
            <h2>Recruitment &amp; Onboarding Workflow Redesign</h2>
            <p>Fragmented forms and untracked candidates replaced with one role-based application, a central tracker, standardised communication, and tracked onboarding.</p>
          </div>
          <div class="cc-metrics">
            <div class="cc-metric"><b>Several weeks &rarr; under 7 days</b><span>Interview scheduling time</span></div>
            <div class="cc-metric"><b>One</b><span>Unified application form</span></div>
            <div class="cc-metric"><b>Centralised</b><span>Candidate tracking</span></div>
          </div>
        </a>

        <a class="case-card reveal" href="/work/instagram-live-series/" aria-label="Case study 02: Instagram Live Series">
          <span class="cc-num">02</span>
          <div>
            <span class="cc-cat mono">Program Development / Volunteer Engagement &middot; The Period Society Rajasthan</span>
            <h2>Instagram Live Series</h2>
            <p>A recurring live format built to give volunteers something to contribute to and the audience a way to ask questions directly.</p>
          </div>
          <div class="cc-metrics">
            <div class="cc-metric"><b>10+</b><span>Instagram Live sessions</span></div>
            <div class="cc-metric"><b>15+</b><span>Speakers coordinated and prepared</span></div>
          </div>
        </a>

        <a class="case-card reveal" href="/work/ending-the-period-stigma/" aria-label="Case study 03: Ending the Period Stigma">
          <span class="cc-num">03</span>
          <div>
            <span class="cc-cat mono">Program Strategy / Initiative Execution &middot; CHRIST University, Bengaluru</span>
            <h2>Ending the Period Stigma</h2>
            <p>A research-based menstrual health awareness initiative, re-routed into a collaborative campus exhibition when the original outreach plan became unfeasible.</p>
          </div>
          <div class="cc-metrics">
            <div class="cc-metric"><b>70+</b><span>Students engaged</span></div>
            <div class="cc-metric"><b>1</b><span>Delivery model rebuilt, objective kept</span></div>
          </div>
        </a>

        <a class="case-card reveal" href="/work/menstrual-health-webinar/" aria-label="Case study 04: Menstrual Health Webinar">
          <span class="cc-num">04</span>
          <div>
            <span class="cc-cat mono">Program Coordination / Educational Content &middot; TPSR &times; Rotaract Club of Dyal Singh College &times; Project Aaina</span>
            <h2>Menstrual Health Webinar</h2>
            <p>Content, speakers, and execution behind a three-way educational collaboration: moderator, content lead, speaker mentor, coordinator, and speaker.</p>
          </div>
          <div class="cc-metrics">
            <div class="cc-metric"><b>~50</b><span>Attendees</span></div>
            <div class="cc-metric"><b>1&ndash;2 weeks</b><span>Speaker preparation</span></div>
            <div class="cc-metric"><b>3 people</b><span>Presentation development</span></div>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- SAMPLES -->
  <section class="section band" id="samples" aria-labelledby="samples-h">
    <div class="wrap">
      <div class="section-head reveal">
        <div>
          <p class="kicker mono">B / Independent work samples</p>
          <h2 id="samples-h">Frameworks, documents, and analytical work.</h2>
        </div>
        <p class="head-copy">Frameworks, documents, and analytical work that offer a closer look at how I approach problems. These were created independently, not delivered inside an organisation.</p>
      </div>

      <div class="sample-rows">
        <a class="sample-row reveal" href="/work/samples/kraftshala-assignment/">
          <div class="sr-visual" aria-hidden="true">
            <div class="doc-thumb doc-thumb--dash">
              <div class="dt-bar mono"><span>Week-on-week dashboard</span><span>Illustrative</span></div>
              <div class="dt-kpis">
                <div class="dt-kpi"><b>44%</b><span>On-time sessions</span></div>
                <div class="dt-kpi"><b>38%</b><span>&ldquo;Other&rdquo; cancellations</span></div>
                <div class="dt-kpi"><b>24.7</b><span>Avg. positive delay (min)</span></div>
              </div>
              <div class="dt-chart">
                <span style="--v:28%"></span><span style="--v:44%"></span><span style="--v:36%"></span>
                <span style="--v:72%"></span><span style="--v:58%"></span><span style="--v:88%"></span>
              </div>
            </div>
          </div>
          <div class="sr-body">
            <span class="mono sr-cat">Work sample 01 &middot; Kraftshala Program Management assignment, 2026</span>
            <h3>Student Experience &amp; Operational Analytics</h3>
            <p>A two-part program management hiring assignment exploring student support, operational problem-solving, and data-driven decision-making.</p>
            <div class="sr-tags">
              <span class="pill">Four-scenario decision framework</span>
              <span class="pill">Five analytical insights</span>
              <span class="pill">Anonymised workbook preview</span>
            </div>
            <span class="link-arrow">Open work sample <span aria-hidden="true">&nearr;</span></span>
          </div>
        </a>

        <a class="sample-row reveal" href="/work/samples/ui-fellowship-presentation/">
          <div class="sr-visual" aria-hidden="true">
            <div class="doc-thumb doc-thumb--deck">
              <div class="dt-slide">
                <span class="mono">Program design</span>
                <strong>Recruitment operating system</strong>
                <div class="dt-slide-nodes"><i></i><i></i><i></i><i></i></div>
              </div>
              <div class="dt-slide dt-slide--ghost">
                <span class="mono">Operating model</span>
                <div class="dt-slide-lines"><i></i><i></i><i></i></div>
              </div>
            </div>
          </div>
          <div class="sr-body">
            <span class="mono sr-cat">Work sample 02 &middot; Hiring process presentation</span>
            <h3>U&amp;I Fellowship &mdash; Program Design &amp; Recruitment Operations</h3>
            <p>A fellowship recruitment and operating model: venue partnership proposal, recruitment leadership structure, recruitment operating system, coordination framework, and timelines.</p>
            <div class="sr-tags">
              <span class="pill">Recruitment operating system</span>
              <span class="pill">Leadership structure</span>
              <span class="pill">Coordination framework</span>
            </div>
            <span class="link-arrow">Open work sample <span aria-hidden="true">&nearr;</span></span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- DOCUMENTATION -->
  <section class="section section--tight" id="documents" aria-labelledby="docs-h" style="border-top:1px solid var(--line)">
    <div class="wrap">
      <div class="section-head reveal">
        <div>
          <p class="kicker mono">C / Organisational documentation</p>
          <h2 id="docs-h">The paperwork that holds a process together.</h2>
        </div>
        <p class="head-copy">Sample documents developed to formalise how a volunteer-led organisation works with its people and partners. Excerpts shown are redacted.</p>
      </div>

      <div class="doc-rows">
        <a class="doc-row reveal" href="/work/samples/volunteer-agreement/">
          <span class="doc-row-num mono">Doc 01</span>
          <div class="doc-row-visual" aria-hidden="true">
            <div class="doc-sheet doc-sheet--sm">
              <div class="ds-head mono">Volunteer Agreement</div>
              <div class="ds-line"></div><div class="ds-line ds-line--short"></div>
              <div class="ds-block"></div>
              <div class="ds-line ds-line--redact"></div>
              <div class="ds-sign"><span></span><span></span></div>
            </div>
          </div>
          <div class="doc-row-body">
            <h3>Volunteer Agreement</h3>
            <span class="mono doc-row-cat">Organisational documentation</span>
            <p>A sample organisational document developed to formalise volunteer expectations, responsibilities, supervision, confidentiality, and other terms of engagement.</p>
            <span class="link-arrow">View redacted excerpts <span aria-hidden="true">&nearr;</span></span>
          </div>
        </a>

        <a class="doc-row reveal" href="/work/samples/memorandum-of-agreement/">
          <span class="doc-row-num mono">Doc 02</span>
          <div class="doc-row-visual" aria-hidden="true">
            <div class="doc-sheet doc-sheet--sm">
              <div class="ds-head mono">Memorandum of Agreement</div>
              <div class="ds-line"></div><div class="ds-line ds-line--short"></div>
              <div class="ds-block"></div>
              <div class="ds-line ds-line--redact"></div>
              <div class="ds-sign"><span></span><span></span></div>
            </div>
          </div>
          <div class="doc-row-body">
            <h3>Memorandum of Agreement</h3>
            <span class="mono doc-row-cat">Organisational documentation</span>
            <p>A sample collaboration document covering scope, responsibilities, terms, funding arrangements, and formal agreement between parties.</p>
            <span class="link-arrow">View redacted excerpts <span aria-hidden="true">&nearr;</span></span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- STRUCTURE -->
  <section class="section section--tight" style="border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:var(--paper)">
    <div class="wrap">
      <p class="kicker mono">How projects are written</p>
      <div class="flow flow--three">
        <div class="flow-step"><span class="n">01</span><span class="t">Context</span><span class="s">The setting and constraints</span></div>
        <div class="flow-step"><span class="n">02</span><span class="t">Problem</span><span class="s">What wasn&rsquo;t working</span></div>
        <div class="flow-step"><span class="n">03</span><span class="t">Approach</span><span class="s">The decisions I made</span></div>
        <div class="flow-step"><span class="n">04</span><span class="t">Execution</span><span class="s">How it was carried out</span></div>
        <div class="flow-step"><span class="n">05</span><span class="t">Outcomes</span><span class="s">What changed, in plain terms</span></div>
        <div class="flow-step"><span class="n">06</span><span class="t">Reflection</span><span class="s">What I took forward</span></div>
      </div>
    </div>
  </section>

  <section class="cta-band">
    <div class="wrap cta-grid">
      <div class="reveal">
        <p class="kicker mono">Start here</p>
        <h2>The recruitment redesign is the <em>centre of gravity.</em></h2>
      </div>
      <div class="reveal" style="--d:.08s">
        <p class="cta-copy">Fragmented forms, untracked candidates, slow onboarding &mdash; and the workflow that replaced all of it.</p>
        <a class="btn btn--light" href="/work/recruitment-onboarding-workflow/">Open case study 01 <span class="arrow" aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </section>
"""

SKILLS = """
  <section class="page-head">
    <div class="wrap">
      <nav class="breadcrumb mono" aria-label="Breadcrumb">
        <a href="/">Home</a><span class="sep" aria-hidden="true">/</span><span>Skills</span>
      </nav>
      <div class="page-head-grid">
        <div>
          <h1>The things I bring to <em>the work.</em></h1>
          <div class="page-lede">
            <p>Grouped by what they are for: running programs, improving processes, coordinating people, and producing content and research.</p>
          </div>
        </div>
        <div class="head-fact reveal">
          <span class="mono">Note</span>
          <dl>
            <dt class="mono">On ratings</dt>
            <dd>No percentages or proficiency scores &mdash; the work samples and case studies are the evidence.</dd>
            <dt class="mono">Learning</dt>
            <dd>Google / Coursera project management certificates, Asana workflow certification, Moodle administration, NIELIT programmes.</dd>
          </dl>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="skill-groups">
        <article class="skill-group reveal">
          <span class="sg-num mono">01</span>
          <h2>Project &amp; Program Operations</h2>
          <div class="skill-tags">
            <span class="skill-tag">Program Operations</span>
            <span class="skill-tag">Project Coordination</span>
            <span class="skill-tag">Initiative Execution</span>
            <span class="skill-tag">Project Tracking</span>
            <span class="skill-tag">Event Coordination</span>
            <span class="skill-tag">Resource Coordination</span>
            <span class="skill-tag">Cross-functional Collaboration</span>
            <span class="skill-tag">Stakeholder Management</span>
          </div>
        </article>

        <article class="skill-group reveal">
          <span class="sg-num mono">02</span>
          <h2>Process Improvement &amp; Systems</h2>
          <div class="skill-tags">
            <span class="skill-tag">Problem Identification</span>
            <span class="skill-tag">Workflow Design</span>
            <span class="skill-tag">Process Improvement</span>
            <span class="skill-tag">Workflow Optimisation</span>
            <span class="skill-tag">Recruitment &amp; Onboarding</span>
            <span class="skill-tag">Knowledge Management</span>
            <span class="skill-tag">Process Documentation</span>
            <span class="skill-tag">Policy Development</span>
          </div>
        </article>

        <article class="skill-group reveal">
          <span class="sg-num mono">03</span>
          <h2>Communication &amp; Coordination</h2>
          <div class="skill-tags">
            <span class="skill-tag">Stakeholder Communication</span>
            <span class="skill-tag">Follow-up Management</span>
            <span class="skill-tag">Meeting Coordination</span>
            <span class="skill-tag">Volunteer Coordination</span>
            <span class="skill-tag">Client Relationship Management</span>
            <span class="skill-tag">Lead Management</span>
            <span class="skill-tag">Training &amp; Facilitation</span>
          </div>
        </article>

        <article class="skill-group reveal">
          <span class="sg-num mono">04</span>
          <h2>Research &amp; Content</h2>
          <div class="skill-tags">
            <span class="skill-tag">Research</span>
            <span class="skill-tag">Curriculum Development</span>
            <span class="skill-tag">Educational Resource Design</span>
            <span class="skill-tag">Audience-centred Content Development</span>
            <span class="skill-tag">Content Writing</span>
            <span class="skill-tag">Script Writing</span>
            <span class="skill-tag">Copywriting</span>
          </div>
        </article>

        <article class="skill-group reveal">
          <span class="sg-num mono">05</span>
          <h2>Tools</h2>
          <div class="skill-tags">
            <span class="skill-tag">Google Workspace</span>
            <span class="skill-tag">Microsoft Excel</span>
            <span class="skill-tag">Google Sheets</span>
            <span class="skill-tag">Asana</span>
            <span class="skill-tag">Notion</span>
            <span class="skill-tag">LeadSquared</span>
            <span class="skill-tag">MCUBE</span>
            <span class="skill-tag">Canva</span>
            <span class="skill-tag">Tally Forms</span>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- CERTIFICATIONS -->
  <section class="section band" id="certifications">
    <div class="wrap">
      <div class="section-head reveal">
        <div>
          <p class="kicker mono">Certifications</p>
          <h2>Structured learning, <em>mostly in project work.</em></h2>
        </div>
        <p class="head-copy">Project management foundations from Google, workflow certification from Asana, and platform and digital programmes alongside them.</p>
      </div>

      <div class="cert-list">
        <a class="cert cert--link reveal" href="https://coursera.org/verify/SXPR3131X6RB" target="_blank" rel="noopener">
          <span class="cn mono">01</span>
          <div>
            <h3>Agile Project Management</h3>
            <p>Google &middot; Coursera</p>
          </div>
          <span class="cert-action mono">Verify <span aria-hidden="true">&nearr;</span></span>
        </a>
        <a class="cert cert--link reveal" href="https://coursera.org/verify/YBW6SFAPSMHY" target="_blank" rel="noopener">
          <span class="cn mono">02</span>
          <div>
            <h3>Foundations of Project Management</h3>
            <p>Google &middot; Coursera</p>
          </div>
          <span class="cert-action mono">Verify <span aria-hidden="true">&nearr;</span></span>
        </a>
        <a class="cert cert--link reveal" href="https://coursera.org/verify/6PY51NTBYOHC" target="_blank" rel="noopener">
          <span class="cn mono">03</span>
          <div>
            <h3>Project Initiation: Starting a Successful Project</h3>
            <p>Google &middot; Coursera</p>
          </div>
          <span class="cert-action mono">Verify <span aria-hidden="true">&nearr;</span></span>
        </a>
        <div class="cert reveal">
          <span class="cn mono">04</span>
          <div>
            <h3>Asana Workflow Specialist</h3>
            <p>Asana &middot; Valid June 9, 2026 &ndash; June 9, 2027</p>
          </div>
          <span class="cert-action mono">Certified</span>
        </div>
        <div class="cert reveal">
          <span class="cn mono">05</span>
          <div>
            <h3>Moodle Administration Settings</h3>
            <p>Moodle Academy</p>
          </div>
        </div>
        <div class="cert reveal">
          <span class="cn mono">06</span>
          <div>
            <h3>Digital Marketing</h3>
            <p>NIELIT</p>
          </div>
        </div>
        <div class="cert reveal">
          <span class="cn mono">07</span>
          <div>
            <h3>Web Designing</h3>
            <p>NIELIT</p>
          </div>
        </div>
      </div>

      <div class="learning-block reveal">
        <h3 class="mono">Additional learning</h3>
        <ul>
          <li><a href="https://coursera.org/verify/UN1UND4M8JGI" target="_blank" rel="noopener">Accelerate Your Job Search with AI &mdash; Google / Coursera <span aria-hidden="true">&nearr;</span></a></li>
          <li><span>Gender and Literature</span></li>
          <li><span>Sport Psychology</span></li>
        </ul>
      </div>

      <div class="recog-block reveal">
        <h3 class="mono">Recognition</h3>
        <div class="recog-items">
          <div class="recog">
            <span class="pill">The Period Society Rajasthan</span>
            <strong>Organisational Mentor</strong>
            <p>Recognition within TPSR supporting the program operations and organisational mentorship responsibilities described on the experience page.</p>
          </div>
          <div class="recog">
            <span class="pill">The Period Society Rajasthan</span>
            <strong>Content Team Head</strong>
            <p>Recognition within TPSR for leading content operations and educational content development with a team of more than 20 members.</p>
          </div>
        </div>
        <p class="mono recog-note">Recognition from the organisation, not external professional certifications.</p>
      </div>
    </div>
  </section>
"""

CONTACT = """
  <section class="page-head">
    <div class="wrap">
      <nav class="breadcrumb mono" aria-label="Breadcrumb">
        <a href="/">Home</a><span class="sep" aria-hidden="true">/</span><span>Contact</span>
      </nav>
      <div class="page-head-grid">
        <div>
          <h1>Have something <em>interesting in motion?</em></h1>
          <div class="page-lede">
            <p>I&rsquo;m interested in opportunities where I can contribute to program execution, operational improvement, and building systems that help teams work better.</p>
          </div>
        </div>
        <div class="head-fact reveal">
          <span class="mono">Direct</span>
          <dl>
            <dt class="mono">Response</dt>
            <dd>Email is the fastest route.</dd>
            <dt class="mono">Open to</dt>
            <dd>Operations, program management, and coordination roles &middot; remote or on-site</dd>
          </dl>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="contact-grid">
        <div class="contact-links">
          <a class="contact-link reveal" href="mailto:i.am.shailly@gmail.com">
            <span class="cl-label mono">Email</span>
            <span class="cl-value">i.am.shailly@gmail.com</span>
            <span class="cl-arrow" aria-hidden="true">&nearr;</span>
          </a>
          <a class="contact-link reveal" href="tel:+917300711147">
            <span class="cl-label mono">Phone</span>
            <span class="cl-value">+91 7300711147</span>
            <span class="cl-arrow" aria-hidden="true">&nearr;</span>
          </a>
          <a class="contact-link reveal" href="https://linkedin.com/in/shailly-presently" target="_blank" rel="noopener">
            <span class="cl-label mono">LinkedIn</span>
            <span class="cl-value">linkedin.com/in/shailly-presently</span>
            <span class="cl-arrow" aria-hidden="true">&nearr;</span>
          </a>
        </div>

        <aside class="contact-aside reveal">
          <div>
            <span class="mono">What I&rsquo;m looking for</span>
            <p>If you&rsquo;re building something, improving how a team works, or looking for someone who enjoys bringing structure to moving parts, I&rsquo;d be happy to hear from you.</p>
          </div>
          <div>
            <span class="mono">Before you write</span>
            <p>If it helps, the work index shows how I approach a problem end to end &mdash; recruitment workflow redesign is the clearest example.</p>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <section class="cta-band">
    <div class="wrap cta-grid">
      <div class="reveal">
        <p class="kicker mono">Next</p>
        <h2>Start with the <em>work.</em></h2>
      </div>
      <div class="reveal" style="--d:.08s">
        <p class="cta-copy">Four projects, two work samples, and two organisational documents &mdash; all in one place.</p>
        <a class="btn btn--light" href="/work/">Selected Work <span class="arrow" aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </section>
"""
