# -*- coding: utf-8 -*-
"""The four implemented project case studies."""

CASE01 = """
  <article>
    <header class="case-hero">
      <div class="wrap">
        <nav class="breadcrumb mono" aria-label="Breadcrumb">
          <a href="/">Home</a><span class="sep" aria-hidden="true">/</span>
          <a href="/work/">Selected Work</a><span class="sep" aria-hidden="true">/</span>
          <span>Case study 01</span>
        </nav>

        <div class="page-head-grid">
          <div>
            <p class="mono case-cat">Operations / Process Improvement</p>
            <h1>From fragmented applications to a connected recruitment and onboarding system.</h1>
          </div>
          <div class="head-fact reveal">
            <span class="mono">Case study 01 / 04</span>
            <dl>
              <dt class="mono">Organisation</dt>
              <dd>The Period Society Rajasthan</dd>
              <dt class="mono">Scope</dt>
              <dd>Recruitment, candidate tracking, onboarding</dd>
              <dt class="mono">Result</dt>
              <dd>Interview scheduling: several weeks &rarr; under seven days</dd>
            </dl>
          </div>
        </div>

        <div class="case-overview">
          <p>Recruitment is one of the first experiences a volunteer has with an organisation. It should be clear, coordinated, and reliable.</p>
          <p>At The Period Society Rajasthan, recruitment had gradually become fragmented &mdash; separate forms, no central record, and onboarding that depended on individual follow-ups.</p>
          <p>I took ownership of redesigning the workflow, from application intake through onboarding.</p>
        </div>
      </div>
    </header>

    <div class="wrap">
      <div class="meta-strip reveal">
        <div class="meta-cell"><span class="k">Organisation</span><span class="v">The Period Society Rajasthan</span></div>
        <div class="meta-cell"><span class="k">Type</span><span class="v">Volunteer-led organisation</span></div>
        <div class="meta-cell"><span class="k">Focus</span><span class="v">Recruitment &amp; onboarding systems</span></div>
        <div class="meta-cell"><span class="k">Used for</span><span class="v">Regular recruitment &amp; Periodt Summer Recruitment Program 2023</span></div>
      </div>
    </div>

    <!-- 01 CONTEXT -->
    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">01</span><h2>Context</h2></div>
        <div class="cs-body">
          <p class="lead">Recruitment had gradually become fragmented.</p>
          <p>Content, Design, and Outreach each had separate application forms and processes, alongside a general application form. This created confusion for applicants and made it difficult to maintain a consolidated view of recruitment.</p>
          <p>Recruitment was largely handled by one person. There was no central record of candidate progress, and different department heads managed processes differently.</p>

          <div class="callout">
            <span class="mono callout-label">The candidate-experience problem</span>
            <p>Applicants were asked to select departments without necessarily understanding what each department did. Some gravitated towards Outreach because they associated it with volunteering and events, even though volunteers from other departments could also participate in events.</p>
          </div>

          <p>Onboarding had similar gaps. Selected candidates could wait one or two weeks for orientation, and there was no consistent tracking of onboarding communication, orientation, or documentation.</p>
        </div>
      </div>
    </section>

    <!-- 02 PROBLEM -->
    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">02</span><h2>The problem</h2></div>
        <div class="cs-body">
          <p class="lead">Five failure points, all connected.</p>

          <div class="sub-block">
            <h3><span class="num">A</span>Too many entry points</h3>
            <p>Separate department forms plus a general form meant applicants had to guess which route applied to them, and there was no single view of who had applied for what.</p>
          </div>
          <div class="sub-block">
            <h3><span class="num">B</span>Dependent on one person</h3>
            <p>With no central record of candidate progress, applications and follow-ups could be missed when that person was stretched.</p>
          </div>
          <div class="sub-block">
            <h3><span class="num">C</span>Different departments, different processes</h3>
            <p>Department heads managed recruitment in their own way, making coordination and visibility across departments difficult.</p>
          </div>
          <div class="sub-block">
            <h3><span class="num">D</span>Roles that were hard to understand</h3>
            <p>Applicants chose departments without knowing what the work actually involved &mdash; so interest and role often did not line up.</p>
          </div>
          <div class="sub-block">
            <h3><span class="num">E</span>Onboarding with no tracking</h3>
            <p>One or two week waits for orientation, with no consistent record of communication, attendance, or documentation.</p>
          </div>

          <div class="ba">
            <div class="ba-col">
              <div class="ba-head mono"><span>Before</span><span>Fig. 01</span></div>
              <ul>
                <li>Separate application forms.</li>
                <li>Fragmented department processes.</li>
                <li>No central candidate tracker.</li>
                <li>Inconsistent communication.</li>
                <li>Untracked onboarding tasks.</li>
              </ul>
            </div>
            <div class="ba-col ba-col--after">
              <div class="ba-head mono"><span>After</span><span>Fig. 02</span></div>
              <ul>
                <li>One role-based application form.</li>
                <li>Shared recruitment visibility.</li>
                <li>Central candidate tracker.</li>
                <li>Standardised communication.</li>
                <li>Tracked onboarding steps.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 03 REDESIGN -->
    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">03</span><h2>The redesign</h2></div>
        <div class="cs-body">
          <p class="lead">Changes that addressed each failure point directly.</p>

          <div class="sub-block">
            <h3><span class="num">1</span>One application entry point</h3>
            <p>I consolidated the separate application forms into a single Tally form.</p>
            <p>Instead of asking applicants to select a department first, I structured the form around the roles they were interested in. This made the application process easier to understand and gave applicants more flexibility to express their interests.</p>
          </div>

          <div class="sub-block">
            <h3><span class="num">2</span>Better candidate&ndash;role matching</h3>
            <p>Applicants could express interest in multiple roles. When someone applied for more than one role, the relevant department heads participated in the interview process. Departments could then assess the candidate and determine where their skills and interests were best suited.</p>
          </div>

          <div class="sub-block">
            <h3><span class="num">3</span>Centralised candidate tracking</h3>
            <p>I built a Google Sheets tracker integrated with Tally so new applications were automatically captured.</p>
            <p>I used the tracker to monitor candidates through a defined sequence of stages:</p>
            <div class="flow" aria-label="Candidate tracking stages">
              <div class="flow-step"><span class="n">Stage 01</span><span class="t">Application received</span></div>
              <div class="flow-step"><span class="n">Stage 02</span><span class="t">Email sent</span></div>
              <div class="flow-step"><span class="n">Stage 03</span><span class="t">Interview scheduled</span></div>
              <div class="flow-step"><span class="n">Stage 04</span><span class="t">Interview completed</span></div>
              <div class="flow-step"><span class="n">Stage 05</span><span class="t">Selection decision</span></div>
              <div class="flow-step"><span class="n">Stage 06</span><span class="t">Candidate informed</span></div>
              <div class="flow-step"><span class="n">Stage 07</span><span class="t">Onboarding initiated</span></div>
              <div class="flow-step"><span class="n">Stage 08</span><span class="t">Onboarded</span></div>
            </div>
          </div>

          <div class="sub-block">
            <h3><span class="num">4</span>Standardised communication</h3>
            <p>I introduced reusable email templates for candidate communication and used interview documents to support the process. I also coordinated interview panels through a WhatsApp group.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 04 ONBOARDING -->
    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">04</span><h2>Onboarding redesign</h2></div>
        <div class="cs-body">
          <p class="lead">Recruitment did not end with a selection decision.</p>
          <p>I took ownership of making sure selected candidates moved through onboarding in a structured way. I tracked:</p>

          <div class="layer-stack" style="margin-top:.4rem">
            <div class="layer-item"><span class="n">01</span><span class="t">Onboarding communication</span><span class="bar" aria-hidden="true"></span></div>
            <div class="layer-item"><span class="n">02</span><span class="t">Orientation scheduling</span><span class="bar" aria-hidden="true"></span></div>
            <div class="layer-item"><span class="n">03</span><span class="t">Orientation attendance</span><span class="bar" aria-hidden="true"></span></div>
            <div class="layer-item"><span class="n">04</span><span class="t">Required document sharing</span><span class="bar" aria-hidden="true"></span></div>
            <div class="layer-item"><span class="n">05</span><span class="t">Document review and completion</span><span class="bar" aria-hidden="true"></span></div>
            <div class="layer-item"><span class="n">06</span><span class="t">Document submission</span><span class="bar" aria-hidden="true"></span></div>
            <div class="layer-item"><span class="n">07</span><span class="t">Storage in the correct locations</span><span class="bar" aria-hidden="true"></span></div>
          </div>

          <p style="margin-top:1.4rem">I also scheduled orientation meetings for new volunteers, so onboarding became a tracked process rather than a series of informal reminders.</p>
        </div>
      </div>
    </section>

    <!-- 05 EXECUTION -->
    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">05</span><h2>Implementation</h2></div>
        <div class="cs-body">
          <p class="lead">The redesigned process was used for regular TPSR recruitment as well as the Periodt Summer Recruitment Program 2023.</p>
          <p>The system connected application intake, candidate tracking, interview coordination, communication, and onboarding into one continuous workflow.</p>

          <div style="margin-top:2rem">
            <div class="mono" style="color:var(--muted);margin-bottom:.9rem">The workflow, end to end &mdash; fig. 03</div>
            <div class="flow" aria-label="Recruitment workflow from application intake to completed onboarding">
              <div class="flow-step"><span class="n">01</span><span class="t">Application intake</span><span class="s">Single Tally form</span></div>
              <div class="flow-step"><span class="n">02</span><span class="t">Candidate tracking</span><span class="s">Sheets, linked to intake</span></div>
              <div class="flow-step"><span class="n">03</span><span class="t">Interview coordination</span><span class="s">Panels and schedule</span></div>
              <div class="flow-step"><span class="n">04</span><span class="t">Selection</span><span class="s">Shared decision</span></div>
              <div class="flow-step"><span class="n">05</span><span class="t">Candidate communication</span><span class="s">Reusable templates</span></div>
              <div class="flow-step"><span class="n">06</span><span class="t">Onboarding</span><span class="s">Tracked steps</span></div>
              <div class="flow-step"><span class="n">07</span><span class="t">Completed onboarding</span><span class="s">Documents stored</span></div>
            </div>
          </div>

          <div class="tracker" role="figure" aria-label="Illustrative candidate tracker interface with fictional sample entries">
            <div class="tracker-bar">
              <span class="mono">TPSR / Candidate Tracker</span>
              <span class="tagline mono">Illustrative &mdash; sample data</span>
            </div>
            <div class="mono tracker-hint" style="padding:.55rem .9rem 0;font-size:.56rem;">Scroll table &rarr;</div>
            <div class="tracker-scroll">
              <table class="track-table">
                <thead>
                  <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Roles interested</th>
                    <th scope="col">Current stage</th>
                    <th scope="col">Communication</th>
                    <th scope="col">Onboarding</th>
                    <th scope="col">Status</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>APP-001</td><td>Content, Social Media</td><td class="stage">Interview scheduled</td>
                    <td>Email sent</td><td>&mdash;</td><td><span class="badge badge--on">Active</span></td>
                  </tr>
                  <tr>
                    <td>APP-002</td><td>Design</td><td class="stage">Interview completed</td>
                    <td>Email sent</td><td>&mdash;</td><td><span class="badge">In review</span></td>
                  </tr>
                  <tr>
                    <td>APP-003</td><td>Outreach, Content</td><td class="stage">Selection decision</td>
                    <td>Email sent</td><td>Initiated</td><td><span class="badge badge--on">Active</span></td>
                  </tr>
                  <tr>
                    <td>APP-004</td><td>Content</td><td class="stage">Onboarded</td>
                    <td>Email sent</td><td>Documents reviewed</td><td><span class="badge">Complete</span></td>
                  </tr>
                  <tr>
                    <td>APP-005</td><td>Design, Outreach</td><td class="stage">Application received</td>
                    <td>Pending</td><td>&mdash;</td><td><span class="badge">New</span></td>
                  </tr>
                  <tr>
                    <td>APP-006</td><td>Social Media</td><td class="stage">Interview completed</td>
                    <td>Email sent</td><td>&mdash;</td><td><span class="badge">In review</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
            <p class="tracker-note"><span class="mark" aria-hidden="true">&#9656;</span> Illustrative interface built for this portfolio. All entries are fictional samples and do not represent candidate data.</p>
          </div>

          <a class="link-card" href="https://www.instagram.com/p/Cr3UZBCvuC7/" target="_blank" rel="noopener" style="margin-top:1.6rem">
            <span class="lc-tag mono">Reference</span>
            <span class="lc-title">Periodt Summer Recruitment Program 2023</span>
            <span class="lc-meta mono">View the post on Instagram <span aria-hidden="true">&nearr;</span></span>
          </a>
        </div>
      </div>
    </section>

    <!-- 06 OUTCOMES -->
    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">06</span><h2>Outcomes</h2></div>
        <div class="cs-body">
          <div class="metrics">
            <div class="metric">
              <span class="big">Several weeks <span class="u">&rarr;</span> under 7 days</span>
              <span class="cap">Improvement in interview scheduling time.</span>
            </div>
            <div class="metric">
              <span class="big">One</span>
              <span class="cap">Unified application form &mdash; a clearer entry point for applicants.</span>
            </div>
            <div class="metric">
              <span class="big">Centralised</span>
              <span class="cap">Candidate tracking &mdash; a shared view of recruitment progress.</span>
            </div>
          </div>
          <p style="margin-top:1.6rem">The unified, role-based application form also led to a noticeable increase in applicants.</p>
          <p>Recruitment progress became easier to see, communication became more structured, and onboarding tasks had clearer follow-through.</p>
        </div>
      </div>
    </section>

    <!-- 07 TOOLS -->
    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">07</span><h2>Tools</h2></div>
        <div class="cs-body">
          <div class="tools">
            <span class="tool">Tally Forms</span>
            <span class="tool">Google Sheets</span>
            <span class="tool">Email templates</span>
            <span class="tool">WhatsApp</span>
            <span class="tool">Interview documentation</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 08 REFLECTION -->
    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">08</span><h2>Reflection</h2></div>
        <div class="cs-body">
          <div class="reflect">
            <p class="q">&ldquo;A process should not depend on someone remembering what needs to happen next.&rdquo;</p>
            <p>Operational problems are often not caused by a lack of effort. They emerge when information, ownership, and next steps are scattered.</p>
            <p>A centralised system does not remove the need for people to coordinate. It makes coordination easier and more reliable.</p>
          </div>
        </div>
      </div>
    </section>

    <div class="wrap">
      <nav class="next-project" aria-label="Next case study">
        <div>
          <span class="mono np-label">Next case study / 02</span>
          <a href="/work/instagram-live-series/"><span class="np-title">Instagram Live Series &rarr;</span></a>
        </div>
        <a class="link-arrow" href="/work/">All selected work <span aria-hidden="true">&nearr;</span></a>
      </nav>
    </div>
  </article>
"""

CASE02 = """
  <article>
    <header class="case-hero">
      <div class="wrap">
        <nav class="breadcrumb mono" aria-label="Breadcrumb">
          <a href="/">Home</a><span class="sep" aria-hidden="true">/</span>
          <a href="/work/">Selected Work</a><span class="sep" aria-hidden="true">/</span>
          <span>Case study 02</span>
        </nav>

        <div class="page-head-grid">
          <div>
            <p class="mono case-cat">Program Development / Volunteer Engagement</p>
            <h1>Creating a recurring space for conversation, participation, and audience engagement.</h1>
          </div>
          <div class="head-fact reveal">
            <span class="mono">Case study 02 / 04</span>
            <dl>
              <dt class="mono">Organisation</dt>
              <dd>The Period Society Rajasthan</dd>
              <dt class="mono">Period</dt>
              <dd>March 2024 &mdash; October 2024</dd>
              <dt class="mono">Result</dt>
              <dd>10+ sessions &middot; 15+ speakers prepared</dd>
            </dl>
          </div>
        </div>

        <div class="case-overview">
          <p>During inactive periods, I noticed gaps in volunteer engagement and direct interaction with the audience.</p>
          <p>Rather than treating social media as only a publishing channel, I saw an opportunity to create a recurring format that would encourage participation, give volunteers opportunities to contribute, and allow the audience to ask questions directly.</p>
          <p>I conceived and launched an Instagram Live initiative for The Period Society Rajasthan.</p>
        </div>
      </div>
    </header>

    <div class="wrap">
      <div class="meta-strip reveal">
        <div class="meta-cell"><span class="k">Organisation</span><span class="v">The Period Society Rajasthan</span></div>
        <div class="meta-cell"><span class="k">Role</span><span class="v">Conceived, designed, hosted, coordinated</span></div>
        <div class="meta-cell"><span class="k">Period</span><span class="v">Mar 2024 &mdash; Oct 2024</span></div>
        <div class="meta-cell"><span class="k">Scale</span><span class="v">10+ sessions &middot; 15+ speakers</span></div>
      </div>
    </div>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">01</span><h2>My contribution</h2></div>
        <div class="cs-body">
          <p class="lead">I designed the session format and content workflow, coordinated speakers, and prepared volunteers to participate confidently.</p>

          <div class="role-grid">
            <div class="role-chip"><span class="mono">01</span><strong>Format design</strong><p>Designed the recurring session format.</p></div>
            <div class="role-chip"><span class="mono">02</span><strong>Speaker coordination</strong><p>Identified and coordinated speakers; prepared more than 15.</p></div>
            <div class="role-chip"><span class="mono">03</span><strong>Content</strong><p>Developed and reviewed session content.</p></div>
            <div class="role-chip"><span class="mono">04</span><strong>Scheduling &amp; logistics</strong><p>Coordinated schedules and session logistics.</p></div>
            <div class="role-chip"><span class="mono">05</span><strong>Practice sessions</strong><p>Ran practice speaking sessions with participants.</p></div>
            <div class="role-chip"><span class="mono">06</span><strong>Briefing</strong><p>Briefed participants on content boundaries, etiquette, and platform conduct.</p></div>
            <div class="role-chip"><span class="mono">07</span><strong>Promotion</strong><p>Supported promotional material and communication.</p></div>
            <div class="role-chip"><span class="mono">08</span><strong>Hosting</strong><p>Hosted and executed sessions; trained volunteers to host independently.</p></div>
          </div>
        </div>
      </div>
    </section>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">02</span><h2>The format</h2></div>
        <div class="cs-body">
          <p class="lead">A repeatable sequence, so each session did not start from zero.</p>
          <div class="flow" aria-label="Recurring Instagram Live session cycle">
            <div class="flow-step"><span class="n">Step 01</span><span class="t">Topic &amp; format</span><span class="s">Shape the session</span></div>
            <div class="flow-step"><span class="n">Step 02</span><span class="t">Speaker</span><span class="s">Identify and coordinate</span></div>
            <div class="flow-step"><span class="n">Step 03</span><span class="t">Content</span><span class="s">Develop and review</span></div>
            <div class="flow-step"><span class="n">Step 04</span><span class="t">Practice</span><span class="s">Prepare and brief</span></div>
            <div class="flow-step"><span class="n">Step 05</span><span class="t">Promotion</span><span class="s">Announce and explain</span></div>
            <div class="flow-step"><span class="n">Step 06</span><span class="t">Live session</span><span class="s">Host and moderate</span></div>
            <div class="flow-step"><span class="n">Step 07</span><span class="t">Next session</span><span class="s">Hand over hosting</span></div>
          </div>
          <p style="margin-top:1.5rem">The same structure was used repeatedly, which made it easier to prepare speakers and to hand hosting responsibilities to volunteers over time.</p>
        </div>
      </div>
    </section>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">03</span><h2>Outcomes</h2></div>
        <div class="cs-body">
          <div class="metrics metrics--two">
            <div class="metric">
              <span class="big">10<span class="u">+</span></span>
              <span class="cap">Instagram Live sessions.</span>
            </div>
            <div class="metric">
              <span class="big">15<span class="u">+</span></span>
              <span class="cap">Speakers coordinated and prepared.</span>
            </div>
          </div>
          <p style="margin-top:1.6rem">Volunteers who had initially been hesitant became more active participants, and some were trained to host sessions independently.</p>
        </div>
      </div>
    </section>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">04</span><h2>Selected posts</h2></div>
        <div class="cs-body">
          <p class="lead">Each session was announced and documented on Instagram. These link directly to the posts.</p>
          <div class="ig-wall">
            <a class="ig-card" href="https://www.instagram.com/p/C5Zq5qmyKAI/" target="_blank" rel="noopener">
              <span class="ig-num mono">01</span>
              <span class="ig-label">Instagram Live</span>
              <span class="ig-link mono">View post <span aria-hidden="true">&nearr;</span></span>
            </a>
            <a class="ig-card" href="https://www.instagram.com/p/C5lBjGCyYBY/" target="_blank" rel="noopener">
              <span class="ig-num mono">02</span>
              <span class="ig-label">Instagram Live</span>
              <span class="ig-link mono">View post <span aria-hidden="true">&nearr;</span></span>
            </a>
            <a class="ig-card" href="https://www.instagram.com/p/C5s4kkSSkdS/" target="_blank" rel="noopener">
              <span class="ig-num mono">03</span>
              <span class="ig-label">Instagram Live</span>
              <span class="ig-link mono">View post <span aria-hidden="true">&nearr;</span></span>
            </a>
            <a class="ig-card" href="https://www.instagram.com/p/C9EoikeN-wy/" target="_blank" rel="noopener">
              <span class="ig-num mono">04</span>
              <span class="ig-label">Instagram Live</span>
              <span class="ig-link mono">View post <span aria-hidden="true">&nearr;</span></span>
            </a>
            <a class="ig-card" href="https://www.instagram.com/p/C-dFk3ETIya/" target="_blank" rel="noopener">
              <span class="ig-num mono">05</span>
              <span class="ig-label">Instagram Live</span>
              <span class="ig-link mono">View post <span aria-hidden="true">&nearr;</span></span>
            </a>
            <a class="ig-card" href="https://www.instagram.com/p/C-pprXRSv8N/" target="_blank" rel="noopener">
              <span class="ig-num mono">06</span>
              <span class="ig-label">Instagram Live</span>
              <span class="ig-link mono">View post <span aria-hidden="true">&nearr;</span></span>
            </a>
          </div>
          <p class="ig-note mono">Post previews are not embedded here &mdash; each card opens the original post on Instagram.</p>
        </div>
      </div>
    </section>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">05</span><h2>What it changed</h2></div>
        <div class="cs-body">
          <div class="reflect">
            <p class="q">&ldquo;The sessions gave volunteers a reason to be involved between campaigns, and gave the audience a place to ask questions directly.&rdquo;</p>
            <p>Social media became a participation channel rather than only a publishing one. The format also created a way to bring new volunteers into public-facing work gradually &mdash; from observing, to speaking, to hosting.</p>
          </div>
        </div>
      </div>
    </section>

    <div class="wrap">
      <nav class="next-project" aria-label="Next case study">
        <div>
          <span class="mono np-label">Next case study / 03</span>
          <a href="/work/ending-the-period-stigma/"><span class="np-title">Ending the Period Stigma &rarr;</span></a>
        </div>
        <a class="link-arrow" href="/work/">All selected work <span aria-hidden="true">&nearr;</span></a>
      </nav>
    </div>
  </article>
"""

CASE03 = """
  <article>
    <header class="case-hero">
      <div class="wrap">
        <nav class="breadcrumb mono" aria-label="Breadcrumb">
          <a href="/">Home</a><span class="sep" aria-hidden="true">/</span>
          <a href="/work/">Selected Work</a><span class="sep" aria-hidden="true">/</span>
          <span>Case study 03</span>
        </nav>

        <div class="page-head-grid">
          <div>
            <p class="mono case-cat">Program Strategy / Initiative Execution</p>
            <h1>Adapting the plan without losing sight of the purpose.</h1>
          </div>
          <div class="head-fact reveal">
            <span class="mono">Case study 03 / 04</span>
            <dl>
              <dt class="mono">Organisation</dt>
              <dd>CHRIST University, Bengaluru</dd>
              <dt class="mono">Period</dt>
              <dd>October 2022 &mdash; November 2022</dd>
              <dt class="mono">Result</dt>
              <dd>70+ students engaged</dd>
            </dl>
          </div>
        </div>

        <div class="case-overview">
          <p>Ending the Period Stigma was a research-based menstrual health awareness initiative that I conceptualised and led.</p>
          <p>The objective was to develop an educational initiative that could address menstrual health awareness through research, accessible educational content, and audience engagement.</p>
        </div>
      </div>
    </header>

    <div class="wrap">
      <div class="meta-strip reveal">
        <div class="meta-cell"><span class="k">Setting</span><span class="v">CHRIST University, Bengaluru</span></div>
        <div class="meta-cell"><span class="k">Role</span><span class="v">Conceptualised and led</span></div>
        <div class="meta-cell"><span class="k">Period</span><span class="v">Oct 2022 &mdash; Nov 2022</span></div>
        <div class="meta-cell"><span class="k">Format</span><span class="v">Campus exhibition</span></div>
      </div>
    </div>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">01</span><h2>The challenge</h2></div>
        <div class="cs-body">
          <p class="lead">The initial approach involved outreach to schools and NGOs.</p>
          <p>However, the planned outreach proved unfeasible within the project&rsquo;s constraints. This created a need to rethink how the initiative could be delivered without losing its core objectives.</p>

          <div class="ba">
            <div class="ba-col">
              <div class="ba-head mono"><span>Original plan</span><span>Fig. 01</span></div>
              <ul>
                <li>Outreach to schools.</li>
                <li>Outreach to NGOs.</li>
                <li>Delivery through partner networks.</li>
                <li>External audience.</li>
              </ul>
            </div>
            <div class="ba-col ba-col--after">
              <div class="ba-head mono"><span>Adapted plan</span><span>Fig. 02</span></div>
              <ul>
                <li>Collaborative campus exhibition.</li>
                <li>In-house audience.</li>
                <li>Same research base.</li>
                <li>Same awareness objective.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">02</span><h2>The pivot</h2></div>
        <div class="cs-body">
          <p class="lead">Instead of abandoning the initiative, I adapted the delivery strategy and shifted towards a collaborative campus exhibition.</p>
          <p>I developed the project strategy, educational content, and engagement approach for the revised format.</p>

          <div class="flow flow--three" aria-label="How the initiative was adapted">
            <div class="flow-step"><span class="n">01</span><span class="t">Objective</span><span class="s">Keep the purpose fixed</span></div>
            <div class="flow-step"><span class="n">02</span><span class="t">Constraints</span><span class="s">Recognise outreach was unfeasible</span></div>
            <div class="flow-step"><span class="n">03</span><span class="t">Route</span><span class="s">Move to a campus exhibition</span></div>
            <div class="flow-step"><span class="n">04</span><span class="t">Content</span><span class="s">Rebuild for the new audience</span></div>
            <div class="flow-step"><span class="n">05</span><span class="t">Delivery</span><span class="s">Collaborative execution</span></div>
            <div class="flow-step"><span class="n">06</span><span class="t">Documentation</span><span class="s">Research and outcomes recorded</span></div>
          </div>
        </div>
      </div>
    </section>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">03</span><h2>Outcome</h2></div>
        <div class="cs-body">
          <div class="metrics metrics--two">
            <div class="metric">
              <span class="big">70<span class="u">+</span></span>
              <span class="cap">Students engaged through the campus exhibition.</span>
            </div>
            <div class="metric">
              <span class="big">On schedule</span>
              <span class="cap">Research, awareness, and documentation objectives met despite the change in delivery approach.</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">04</span><h2>Reflection</h2></div>
        <div class="cs-body">
          <div class="reflect">
            <p class="q">&ldquo;Plans are useful, but the ability to adapt them is just as important.&rdquo;</p>
            <p>This project reinforced the importance of separating the objective from the original execution plan. When one route becomes unfeasible, the work is to find another route that still serves the purpose.</p>
          </div>
        </div>
      </div>
    </section>

    <div class="wrap">
      <nav class="next-project" aria-label="Next case study">
        <div>
          <span class="mono np-label">Next case study / 04</span>
          <a href="/work/menstrual-health-webinar/"><span class="np-title">Menstrual Health Webinar &rarr;</span></a>
        </div>
        <a class="link-arrow" href="/work/">All selected work <span aria-hidden="true">&nearr;</span></a>
      </nav>
    </div>
  </article>
"""

CASE04 = """
  <article>
    <header class="case-hero">
      <div class="wrap">
        <nav class="breadcrumb mono" aria-label="Breadcrumb">
          <a href="/">Home</a><span class="sep" aria-hidden="true">/</span>
          <a href="/work/">Selected Work</a><span class="sep" aria-hidden="true">/</span>
          <span>Case study 04</span>
        </nav>

        <div class="page-head-grid">
          <div>
            <p class="mono case-cat">Program Coordination / Educational Content</p>
            <h1>Building the content, people, and execution behind an educational collaboration.</h1>
          </div>
          <div class="head-fact reveal">
            <span class="mono">Case study 04 / 04</span>
            <dl>
              <dt class="mono">Collaboration</dt>
              <dd>Rotaract Club of Dyal Singh College &times; Project Aaina &times; The Period Society Rajasthan</dd>
              <dt class="mono">Role</dt>
              <dd>TPSR representative, lead content creator, moderator, speaker mentor, event coordinator, speaker</dd>
            </dl>
          </div>
        </div>

        <div class="case-overview">
          <p>I represented The Period Society Rajasthan in a collaborative educational webinar on menstrual health organised with Rotaract Club of Dyal Singh College and Project Aaina.</p>
          <p>The initiative brought together educational content, speaker participation, and audience engagement in an online session attended by approximately 50 people.</p>
        </div>
      </div>
    </header>

    <div class="wrap">
      <div class="meta-strip reveal">
        <div class="meta-cell"><span class="k">Partners</span><span class="v">Rotaract Club of Dyal Singh College &middot; Project Aaina &middot; TPSR</span></div>
        <div class="meta-cell"><span class="k">Roles</span><span class="v">Six, across content and delivery</span></div>
        <div class="meta-cell"><span class="k">Attendance</span><span class="v">Approximately 50</span></div>
        <div class="meta-cell"><span class="k">Prep</span><span class="v">1&ndash;2 weeks of speaker preparation</span></div>
      </div>
    </div>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">01</span><h2>My roles</h2></div>
        <div class="cs-body">
          <p class="lead">The work spanned content, people, and live delivery.</p>
          <div class="role-grid role-grid--six">
            <div class="role-chip"><span class="mono">01</span><strong>Moderator</strong></div>
            <div class="role-chip"><span class="mono">02</span><strong>TPSR representative</strong></div>
            <div class="role-chip"><span class="mono">03</span><strong>Lead content creator</strong></div>
            <div class="role-chip"><span class="mono">04</span><strong>Speaker mentor</strong></div>
            <div class="role-chip"><span class="mono">05</span><strong>Event coordinator</strong></div>
            <div class="role-chip"><span class="mono">06</span><strong>Speaker</strong></div>
          </div>
        </div>
      </div>
    </section>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">02</span><h2>My contribution</h2></div>
        <div class="cs-body">
          <p class="lead">I worked on the complete educational content structure, session script, and presentation framework.</p>
          <p>I collaborated with two designers from the TPSR team to create the presentation deck used during the webinar.</p>
          <p>I also prepared participating speakers through practice sessions and public-speaking preparation over approximately one to two weeks.</p>
          <p>Alongside content preparation, I coordinated with external collaborators and internal TPSR teams regarding scheduling, rehearsals, speaker flow, content planning, promotional timelines, and execution logistics.</p>

          <div class="callout">
            <span class="mono callout-label">On the live session</span>
            <p>During the live webinar, another team member delivered the presentation. I coordinated the slide transitions, moderated the discussion and audience Q&amp;A, and participated as a speaker myself.</p>
          </div>

          <div style="margin-top:2rem">
            <div class="mono" style="color:var(--muted);margin-bottom:.9rem">Content development &mdash; fig. 01</div>
            <div class="flow" aria-label="Content development and delivery workflow">
              <div class="flow-step"><span class="n">01</span><span class="t">Research</span><span class="s">Educational content base</span></div>
              <div class="flow-step"><span class="n">02</span><span class="t">Structure</span><span class="s">Session framework</span></div>
              <div class="flow-step"><span class="n">03</span><span class="t">Script</span><span class="s">Presentation flow</span></div>
              <div class="flow-step"><span class="n">04</span><span class="t">Deck</span><span class="s">With two TPSR designers</span></div>
              <div class="flow-step"><span class="n">05</span><span class="t">Rehearsal</span><span class="s">Speaker preparation</span></div>
              <div class="flow-step"><span class="n">06</span><span class="t">Live session</span><span class="s">Delivery and moderation</span></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">03</span><h2>Outcomes</h2></div>
        <div class="cs-body">
          <div class="metrics">
            <div class="metric">
              <span class="big">~50</span>
              <span class="cap">Attendees at the live session.</span>
            </div>
            <div class="metric">
              <span class="big">1&ndash;2 weeks</span>
              <span class="cap">Of speaker preparation and practice.</span>
            </div>
            <div class="metric">
              <span class="big">3 people</span>
              <span class="cap">Presentation development collaboration.</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">04</span><h2>Evidence</h2></div>
        <div class="cs-body">
          <p class="lead">The session announcement and the content materials behind it.</p>
          <div class="link-cards">
            <a class="link-card" href="https://www.instagram.com/p/C5-jtwISuNj/" target="_blank" rel="noopener">
              <span class="lc-tag mono">Announcement</span>
              <span class="lc-title">Webinar announcement post</span>
              <span class="lc-meta mono">View on Instagram <span aria-hidden="true">&nearr;</span></span>
            </a>
            <a class="link-card" href="https://drive.google.com/drive/folders/1AwQ97QJj0A2Io8I74eOP8lNieBMATTdl?usp=drive_link" target="_blank" rel="noopener">
              <span class="lc-tag mono">Materials</span>
              <span class="lc-title">Webinar content &amp; presentation materials</span>
              <span class="lc-meta mono">Open the Drive folder <span aria-hidden="true">&nearr;</span></span>
            </a>
          </div>

          <div class="evidence-note">
            <span class="mono">On visuals</span>
            <p>The webinar poster and presentation deck live in the links above. They are not reproduced here because the original files include third-party content and speaker materials.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="cs-section">
      <div class="wrap cs-grid">
        <div class="cs-label"><span class="n">05</span><h2>Reflection</h2></div>
        <div class="cs-body">
          <div class="reflect">
            <p class="q">&ldquo;Educational sessions depend on more than the information being presented.&rdquo;</p>
            <p>The content, preparation, coordination, and audience experience all need to work together. Most of the work happened before the session went live &mdash; and that preparation is what made the live hour feel simple.</p>
          </div>
        </div>
      </div>
    </section>

    <div class="wrap">
      <nav class="next-project" aria-label="Next work">
        <div>
          <span class="mono np-label">Next / Work samples</span>
          <a href="/work/samples/kraftshala-assignment/"><span class="np-title">Student Experience &amp; Operational Analytics &rarr;</span></a>
        </div>
        <a class="link-arrow" href="/work/">All selected work <span aria-hidden="true">&nearr;</span></a>
      </nav>
    </div>
  </article>
"""
